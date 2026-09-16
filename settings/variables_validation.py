from groupinfo import *

# Variable settings, these may be modified

# Configuration of the objectives to be simulated by the simulator
# Select optimizations automatically based on the groupinfo.py information provided or not:
objectives = []
objectives_losses = []

if optimize_greedy:
    objectives.append("optimize_greedy")
if optimize_prices:
    objectives.append("optimize_prices")
# if optimize_co2:
#     objectives.append("optimize_co2")
if optimize_self:
    objectives.append("optimize_self_consumption")
if optimize_flat:
    objectives.append("optimize_profile_flatness")




# In case we want to test specific houses
cfg_houses = {
    # default config
    0: {    # <- This is the house number
        # PV configuration
        "pvpanels":  10,  # Number of panels, integer
        "pvazimuth": "southeast",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  40,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  5,  # Capacity in kWh
        "batsoc":       2,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -3000,  # Minumum power (discharge is negative) in W
        "batpmax":      3000,  # Maximum power in W
    },

    # Second house: # NOTE THE OFF-BY-ONE COUNTING!
    1: {
        # PV configuration
        "pvpanels":  10,  # Number of panels, integer
        "pvazimuth": "southwest",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  40,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  5,  # Capacity in kWh
        "batsoc":       2,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -3000,  # Minumum power (discharge is negative) in W
        "batpmax":      3000,  # Maximum power in W
    },

    # FOR SIZING EXCERISE:
    # Third house, this is one of the houses to use for sizing
    2: {
        # PV configuration
        "pvpanels":  0,  # Number of panels, integer
        "pvazimuth": "south",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  30,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  0,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -0,  # Minumum power (discharge is negative) in W
        "batpmax":      0,  # Maximum power in W
    },
    
    # Fourth house, this is one of the houses to use for sizing
    3: {
        # PV configuration
        "pvpanels":  0,  # Number of panels, integer
        "pvazimuth": "south",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  30,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  0,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -0,  # Minumum power (discharge is negative) in W
        "batpmax":      0,  # Maximum power in W
    },
    
    
    
    
    # Normal house
    28: {
        # PV configuration
        "pvpanels":  7,  # Number of panels, integer
        "pvazimuth": "south",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  40,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  3,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -3000,  # Minumum power (discharge is negative) in W
        "batpmax":      3000,  # Maximum power in W
    },


    # Default style house
    50: {
        # PV configuration
        "pvpanels":  6,  # Number of panels, integer
        "pvazimuth": "west",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  35,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 1,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  3,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -3000,  # Minumum power (discharge is negative) in W
        "batpmax":      3000,  # Maximum power in W
    },

    #House with significant EV demand and no RES
    49: {
        # PV configuration
        "pvpanels":  0,  # Number of panels, integer
        "pvazimuth": "south",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  40,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  0,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -0000,  # Minumum power (discharge is negative) in W
        "batpmax":      0000,  # Maximum power in W
    },

    # House with RES, but no battery
    56: {
        # PV configuration
        "pvpanels":  6,  # Number of panels, integer
        "pvazimuth": "east",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  45,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 2,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  0,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -0000,  # Minumum power (discharge is negative) in W
        "batpmax":      0000,  # Maximum power in W
    },

    # NO RES, but battery
    63: {
        # PV configuration
        "pvpanels":  0,  # Number of panels, integer
        "pvazimuth": "east",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  45,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  3,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -3000,  # Minumum power (discharge is negative) in W
        "batpmax":      3000,  # Maximum power in W
    },
}



cfg_scores = {
    # First house:  # NOTE THE OFF-BY-ONE COUNTING!
    44: {
        # PV configuration
        "pvpanels":  7,  # Number of panels, integer
        "pvazimuth": "south",  # Available options: east, southeast, south, southwest, west
        "pvtilt":  40,  # Available options: 10, 15, 20, 25, 30, 35, 40, 45, 50

        # Wind turbine configuration
        "winddiameter": 0,  # Diameter in metres

        # Battery configuration
        "batminsoc":    0,  # Minimum state of charge in kWh
        "batcapacity":  3,  # Capacity in kWh
        "batsoc":       0,  # Initial State of Charge at start of simulation in kWh
        "batpmin":      -3000,  # Minumum power (discharge is negative) in W
        "batpmax":      3000,  # Maximum power in W
    },
}
