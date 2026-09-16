from settings.constants import *
from helpers.helpers import *
import copy

# external classes
from battery.batterysim import *
from battery.batterygreedy import *
from battery.batteryprices import *
from battery.batteryco2 import *
from battery.batteryself import *
from battery.batteryflat import *

class Battery():
    def __init__(self, house):
        self.name = "Battery"
        self.house = house
        self.number = self.house.housenumber
        self.cfg_houses = self.house.cfg_houses
        self.type = "storage"

        # Placeholder, will be loaded upon initialize()
        self.batsoc = 0
        self.batminsoc = 0
        self.batcapacity = 0
        self.batpmin = 0
        self.batpmax = 0

        self.initialize()

        # Planning/control variable
        self.planning = []  # This list contains the control actions required

    # Simulation code
    def execute(self, objective, prices, co2, profile):
        # initialize the device
        self.initialize()

        # pre validation
        if not self.verify_input():
            print("The input parameters for device " + str(self.name) + " of house "+str(self.number) +" are invalid! Aborting! Most likely you have not added (enough) values to the profile list using profile.append(<value>).")
            exit()

        # Perform the optimization
        planning = self.optimize(objective, copy.deepcopy(prices), copy.deepcopy(co2), copy.deepcopy(profile))
        if not self.verify_planning(planning):
            print("The optimization algorithm for device " + str(self.name) + " yields invalid results! Aborting! Most likely you have not added (enough) values to the planninglist using planning.append(<value>).")
            exit()

        # Perform the simulation
        returnprofile = self.simulate(copy.deepcopy(planning))
        if not self.verify_result(returnprofile):
            print("The simulation of device " + str(self.name) + " failed! Aborting! Most likely you are violating our constraints. Carefully read the error log above and the comments in the code that caused the crash.")
            exit()

        self.profile = returnprofile
        return self.profile

    # Function to initialize the results
    def initialize(self, resetLists = True):
        if resetLists:
            # initialize with empty profile
            self.profile = [0] * cfg_sim['intervals']
            self.planning = [0] * cfg_sim['intervals']

        # Battery settings
        try:
            self.batsoc = self.cfg_houses[self.number]["batsoc"]
            self.batminsoc = self.cfg_houses[self.number]["batminsoc"]
            self.batcapacity = self.cfg_houses[self.number]["batcapacity"]
            self.batpmin = self.cfg_houses[self.number]["batpmin"]
            self.batpmax = self.cfg_houses[self.number]["batpmax"]
        except:
            print("Input for battery " + str(self.number) + " is invalid! Most likely you are violating our constraints. Carefully read the error log above and the comments in the code that caused the crash.")
            exit()

    # Optimization code
    def optimize(self, objective, prices, co2, profile):
        self.initialize(False)
        planning = [0] * cfg_sim['intervals']

        if objective == "optimize_greedy":
            return batterygreedy(copy.deepcopy(self), copy.deepcopy(prices), copy.deepcopy(co2), copy.deepcopy(profile))

        elif objective == "optimize_prices":
            # Perform price optimization
            return batteryprices(copy.deepcopy(self), copy.deepcopy(prices), copy.deepcopy(co2), copy.deepcopy(profile))

        elif objective == "optimize_co2":
            # Perform CO2 emissions reduction
            return batteryco2(copy.deepcopy(self), copy.deepcopy(prices), copy.deepcopy(co2), copy.deepcopy(profile))

        elif objective == "optimize_self_consumption":
            # Perform self-consumption optimization
            return batteryself(copy.deepcopy(self), copy.deepcopy(prices), copy.deepcopy(co2), copy.deepcopy(profile))

        elif objective == "optimize_profile_flatness":
            # Optimize the device power profile towards a flat profile using the Euclidean distance vector norm (2-norm)
            return batteryflat(copy.deepcopy(self), copy.deepcopy(prices), copy.deepcopy(co2), copy.deepcopy(profile))

        else:
            # Default fallback
            return planning

    # Simulation code
    def simulate(self, planning=[]):
        self.initialize(False)
        return batterysim(copy.deepcopy(self), copy.deepcopy(planning))

    # Function to verify the created planning by the optimization code
    # But also to verify user input, is it valid input?
    def verify_input(self):
        assert (self.batcapacity >= 0)                  # Battery capacity must be positive
        assert (self.batminsoc >= 0)                    # Battery minimum SoC must be equal or more than 0
        assert (self.batsoc >= 0)                       # Battery current SoC must be equal or more than 0
        assert (self.batsoc <= self.batcapacity)        # Battery current SoC must be smaller or equal to the capacity
        assert (self.batminsoc <= self.batcapacity)     # Battery current SoC must be equal or more than the minimum SoC
        assert (self.batpmin <= self.batpmax)           # Battery power must be smaller or equal to the maximum allowed power

        if self.batpmin < self.batcapacity*cfg_sim['bat_maxcrate']*-1000:
            print("Input for battery " + str(self.number) + " is invalid! The minimum power (batpmin) may not be lower than -"+str(cfg_sim['bat_maxcrate'])+" C-rate. The lowest allowed value given its capacity is: "+str( self.batcapacity*cfg_sim['bat_maxcrate']*-1000))
            exit()
        if self.batpmax > self.batcapacity*cfg_sim['bat_maxcrate']*1000:
            print("Input for battery " + str(self.number) + " is invalid! The maximumpower (batpmax) may not be higher than -"+str(cfg_sim['bat_maxcrate'])+" C-rate. The highest allowed value given its capacity is: "+str( self.batcapacity*cfg_sim['bat_maxcrate']*1000))
            exit()

        return True

    def verify_planning(self, planning):
        self.initialize(False)
        assert (len(self.planning) == cfg_sim['intervals']) # The planning list must be as long as the number of simulation time intervals
        return True

    # Function to verify if the code functions correctly
    def verify_result(self, profile):
        self.initialize(False)
        assert (len(self.profile) == cfg_sim['intervals']) # The power profile list must be as long as the number of simulation time intervals

        # Internal conversion to Wtau
        capacity = 1000 * (3600 / cfg_sim['timebase']) * self.batcapacity
        soc = 1000 * (3600 / cfg_sim['timebase']) * self.batsoc
        minsoc = 1000 * (3600 / cfg_sim['timebase']) * self.batminsoc

        assert (len(profile) == cfg_sim['intervals'])
        for value in profile:
            assert (value >= self.batpmin)	# The power drawn must be at least the minimum power (maximal discharging)
            assert (value <= self.batpmax)	# The power drawn must be at most the maximum power (maximal charging)

            # determine if the SoC at the end of the interval will be in bounds
            soc += value

            assert (soc >= minsoc - 0.1)	# The SoC must remain positive. Are you discharging too much?
            assert (soc <= capacity + 0.1)	# The SoC cannot be higher than the capacity. Are you charging too much?
        return True
