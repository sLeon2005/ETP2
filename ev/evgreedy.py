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
def evgreedy(ev, prices, co2, profile):
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

    # Implementation of the greedy variant:
    for i in range(0, len(profile)):
        planning.append(evpmax)

    # Finally, the resulting planning for the device must be returned
    return planning