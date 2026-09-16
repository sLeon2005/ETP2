from settings.constants import *

# Check if the script is not executed directly, but called through simulator or a test script
import sys
import os
if os.path.basename(sys.argv[0]) != 'simulator.py' and os.path.basename(sys.argv[0])[:4] != 'test':
    print("ERROR: You cannot directly execute this file, but need to execute simulator.py or a test script")
    quit()

    
import math
import random

# With this function, a planning for the operation (i.e. control actions) can be implemented

# Function arguments:
#
# Input:
#   - ev:       Object representing the data structure of EV properties (see comments below)
#   - prices:   A vector (list) representing the electricity price per interval (element)
#   - co2:      A vector (list) representing the CO2 emissions from the national energy mix per interval (element)
#   - profile:  A vector (list) representing the aggregated load and generation of other devices in the house per interval. This is: base load, PV and wind generation
#
# Returns:
#   - planning: A vector (list) representing the planned power values per interval (per your implemented algorithm) in Watts
#
# Notes: 
#   - the length of planning (i.e., number of elements) must equal the lenghth of the profile list (input)
#   - use the input arguments as read only!
#   - assume len(prices) == len(co2) == len(profile) 
#   - With default settings this is 672 elements (7 days times 96 intervals (of 15 mins) per day)
#   - Do not change the function definition on the next line
def evflat(ev, prices, co2, profile):
    # result parameter to be filled and returned in the end:
    planning = []

    # preparing local usage variables for the EV state:
    evsoc = ev.evsoc
    evminsoc = ev.evminsoc  
    evcapacity = ev.evcapacity      
    evpmin = ev.evpmin             
    evpmax = ev.evpmax           
    evenergy = ev.evenergy          
    evarrivalhour = ev.evarrivalhour
    evconnectiontime = ev.evconnectiontime
    tau = cfg_sim['tau']
  

    # NOTE: The following variables help in the implementation of the code
    # NOTE: TREAT THESE VARIABLES AS READ-ONLY!

    # ev parameters and variables are defined as follows:
    # evsoc              # State of Charge of the EV in kWh
    # evminsoc           # Minimum State of Charge of the EV in kWh (because of driving)
    # evcapacity         # Capacity of the EV in kWh
    # evpmin             # Minimum power of the EV in W = 0 W (EV cannot discharge. No V2G is possible.)
    # evpmax             # Maximum power of the EV in W
    # evenergy           # Energy consumption of the EV over one driving session in kWh

    # Timing variables are defined as follows:
    # evconnectiontime   # Hours the EV is connected
    # evarrivalhour      # Hour of arrival of the EV each day

    # NOTE: The EV needs to be fully charged (i.e., reach maximum SoC) when departing

    # Other input
    # The profile vector provides values in Watt for each discrete interval (to be complete, this is the average power consumption in W during an interval)
    # Negative values indicate overproduction.
    
   

    # FIXME: Placeholder implementation to run initial simulations
    ### PLEASE REMOVE THE CODE BELOW BETWEEN THE LINES AND CODE YOUR OWN IMPLEMNETATION ###
            
    #######################################################################################
    first = True
    for i in range(0, len(profile)):
        if first:
            print("WARNING: You have not removed the placeholder code from the EV optimization. Please read the comments in the code. See file ev/evgflat.py")
            first = False
        # Static charging at maximum power
        planning.append(evpmax)
    #######################################################################################

    # FIXME: IMPLEMENT YOUR OWN CODE BELOW IN THE FOR-LOOP
    


    # Your task is to modify the code such that the list containing the planning is filled. 
    # This is also a list, with each value representing the power consumption (average) during an interval in Watts
    # The length of this list must be equal to the input vectors (i.e., prices, co2 and profile)

    # For each interval i, these can be set by adding the correction value to the planning list, i.e.:
    # planning.append(<your_value>)
    # NOTE: Make sure that at the end the number of elements in the planning equals the (original) length of the profile vector

    # NOTE: The given code does not include that the state of charge (SoC) of the EV battery is reduced due to driving
    # For this assignment you will need to implement SoC bookkeeping yourself and ensure that it stays within capacity bounds 
    # Tip: Use the "evenergy" variable for this in your code



    # What is already given is to determine if the EV is connected to the charging station (at home) or not (driving)
    intervals_per_day = (3600 / cfg_sim['timebase']) * 24
    intervals_per_hour = (3600 / cfg_sim['timebase'])

    # Looping through the provided profile vector (this equals looping through time)
    for i in range(0, len(profile)):
        # Note that this for-statement would essentially step through the profile as if it were a discrete time simulation
        # check availability:
        arrival_day = math.floor(i/intervals_per_day)
        arrival_interval = int(arrival_day*intervals_per_day + ev.evarrivalhour * intervals_per_hour)
        departure_interval = int(arrival_interval + ev.evconnectiontime * intervals_per_hour)

        # Check for overruns:
        if ev.evarrivalhour+ev.evconnectiontime >= 24:
            if departure_interval - (24 * (3600 / cfg_sim['timebase'])) >= i and arrival_interval - (24 * (3600 / cfg_sim['timebase'])) > 0:
                departure_interval -= int(24 * (3600 / cfg_sim['timebase']))
                arrival_interval -= int(24 * (3600 / cfg_sim['timebase']))


        # FIXME Here you will need to implement the behaviour of the electric vehicle (read the NOTE and TIP at the end of this file too)
        #       You do not necessarily need to use all if-constructs, but they are defined for your confenience if you wish to make use of them
        #       Keep the "pass" if you do not want to use one of the if-constructs, otherwise the pass command may be removed.

        if i == arrival_interval:
            # Moment at which the EV arrives
            pass

        if i >= arrival_interval and i < departure_interval:
            # Interval that the EV is connected (available)
            pass

        else:
            # Interval that the EV is disconnected (unavailable)
            pass

        if i == departure_interval:
            # Moment at which the EV departs
            pass

        # NOTE: You will need to do two things:
        #       1. Update the SoC of the EV at the right time (see Lecture 2) by deducting the energy of a driving session
        #       2. Create the code to optimize the power profile of the EV
        #
        # TIP:  A possible approach is to plan the charging process of a charging session at once when the car arrives.
        #       Afterall, we are planning/scheduling, which means that we can plan the charging for the time intervals that are still to come (we assume perfect knowledge).
        #       For the indices, you can make use of these 2 variables: arrival_interval and departure_interval.
        #       Furthermore, a specific slice a list can be created as: new_list = old_list[start_index:end_index]

    
    # Finally, the resulting planning for the device must be returned
    return planning