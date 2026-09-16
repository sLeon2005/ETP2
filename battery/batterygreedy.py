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
#   - battery:  Object representing the data structure of battery properties (see comments below)
#   - prices:   A vector (list) representing the electricity price per interval (element)
#   - co2:      A vector (list) representing the CO2 emissions from the national energy mix per interval (element)
#   - profile:  A vector (list) representing the aggregated load and generation of other devices in the house per interval. This is: base load, EV, PV and wind generation
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
def batterygreedy(battery, prices, co2, profile):
    # FIXME: This is a placeholder that needs to be implemented

    # result parameter:
    planning = []

    # preparing local usage variables for the battery state:
    batsoc = battery.batsoc        
    batminsoc = battery.batminsoc    
    batcapacity = battery.batcapacity   
    batpmin = battery.batpmin       
    batpmax = battery.batpmax  
    tau = cfg_sim['tau']    
  

    # NOTE: The following variables help in the implementation of the code
    # NOTE: TREAT THESE VARIABLES AS READ-ONLY!
    
    # Battery parameters and variables are defined as follows:
    # batsoc        # State of Charge in kWh
    # batminsoc     # Minimum State of Charge in kWh
    # batcapacity   # Capacity of the battery in kWh
    # batpmin       # Minimum power in W (Negative value)
    # batpmax       # Maximum power in W

    # Other input
    # The profile vector provides values in Watt for each discrete interval (to be complete, this is the average power consumption in W during an interval)
    # Negative values indicate overproduction.

    # Implementation
    for i in range(0, len(profile)):
        planning.append(-profile[i])


    # Finally, the resulting planning for the device must be returned
    return planning