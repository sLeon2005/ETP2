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
def batteryflat(battery, prices, co2, profile):
    # FIXME: This is a placeholder that needs to be implemented

    # result parameter:
    planning = [0] * len(profile)
    #planning = []
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



    # Your task is to modify the code such that the list containing the planning is filled. 
    # This is also a list, with each value representing the power consumption (average) during an interval in Watts
    # The length of this list must be equal to the input vectors (i.e., prices, co2 and profile)

    # For each interval i, these can be set by adding the correction value to the planning list, i.e.:
    # planning.append(<your_value>)
    # NOTE: Make sure that at the end the number of elements in the planning equals the (original) length of the profile vector

    # NOTE: The given code does not include the state of charge (SoC) of the battery
    # For this assignment you will need to implement SoC bookkeeping yourself and ensure that it stays within capacity bound


    # FIXME: Placeholder implementation to run simulations
    ### PLEASE REMOVE THE CODE BELOW BETWEEN THE LINES AND CODE YOUR OWN IMPLEMENTATION ###
    
    #######################################################################################
    '''
    first = True
    for i in range(0, len(profile)):
        if first:
            print("WARNING: You have not removed the placeholder code from the battery optimization. Please read the comments in the code. See file battery/batteryflat.py")
            first = False
        # Static charging at 0.0 W
        planning.append(0.0)
    return planning
    '''
    #######################################################################################

    n = len(profile)

    lower = min(profile[i] + batpmin for i in range(n))
    upper = max(profile[i] + batpmax for i in range(n))

    for k in range(100):
        bisection = (lower + upper) / 2
        total_power = 0
        for i in range(n):
            total_power += max(batpmin, min(bisection-profile[i], batpmax))

        if total_power < (batcapacity - batsoc) / tau:
            lower = bisection
        else:
            upper = bisection
        if upper-lower < 1e-9:
            break

    bisection = (lower+upper)/2
    session_p = [0]*n
    for i in range(n):
        session_p[i] = max(batpmin, min(bisection - profile[i], batpmax))

    for i in range(n):
        remaining_intervals = n - i - 1
        if i == 0:
            previous_soc = batsoc
        else:
            total = 0
            for j in range(i):
                total += planning[j]
            previous_soc = batsoc+tau*total

        minimum_soc = max(batminsoc, batcapacity - remaining_intervals * batpmax * tau)
        maximum_soc = min(batcapacity, batcapacity - remaining_intervals * batpmin * tau)

        desired_soc = previous_soc + tau * session_p[i]
        next_soc = max(minimum_soc, min(desired_soc, maximum_soc))
        planning[i] = max(batpmin, min(((next_soc - previous_soc) / tau), batpmax))

    for k in range(100):
        soc = [0]*n
        soc_value = batsoc
        for i in range(n):
            soc_value += tau*planning[i]
            soc[i] = soc_value

        for i in range(n - 1):
            a = profile[i] + planning[i]
            b = profile[i+1] + planning[i+1]

            if a < b:
                delta = min(((b-a)/2),(batpmax-planning[i]),(planning[i+1]-batpmin),((batcapacity-soc[i])/tau))
                if delta > 0:
                    planning[i] += delta
                    planning[i+1] -= delta
                    soc[i] += tau*delta

            elif a > b:
                delta = min(((a - b) / 2), (planning[i] - batpmin), (batpmax - planning[i + 1]),
                            ((soc[i] - batminsoc) / tau))
                if delta > 0:
                    planning[i] -= delta
                    planning[i+1] += delta
                    soc[i] -= tau*delta

    for i in range(n):
        planning[i] = max(batpmin,min(batpmax,planning[i]))







    # Finally, the resulting planning for the device must be returned
    return planning