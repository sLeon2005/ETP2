# Constant variables used for the simulation
# DO NOT CHANGE THIS FILE!

cfg_sim = {}

# General settings
cfg_sim['timebase']         = 900   # Interval length in seconds
cfg_sim['intervals']        = 7*96  # Discrete time intervals to simulate
cfg_sim['startInterval']    = 0     # Discrete time interval to start the simulation

# Definition of Tau
cfg_sim['ivperhour']        = 3600 / cfg_sim['timebase']  # Intervals per hour
cfg_sim['tau']              = 1 / (1000*cfg_sim['ivperhour'])  # Conversion factor: Watts for one interval -> kWh for that interval

# Result folder
cfg_sim['outputfile']       = "output/results.csv"
cfg_sim['overviewfile']     = "output/overview.csv"

# Device and house specific limits
cfg_sim['bat_maxcrate']     = 1     # Maximum c-rate allowed for battery
cfg_sim['bat_maxcapacity']  = 0.5   # Maximum capacity as ratio of the average daily electricity demand
cfg_sim['wind_maxdiameter'] = 5     # Maximum wind turbine diameter
cfg_sim['res_coverage']     = 2     # Maximum ratio of supply/demand of res (pv and wind)

# Verification of module imports
# allowed (standard) modules:
cfg_sim['mod_allowlist']    = ['sys', 'builtins', '_frozen_importlib', '_imp', '_thread', '_warnings', '_weakref', '_io', 'marshal', 'posix', '_frozen_importlib_external', 'time', 'zipimport', '_codecs', 'codecs', 'encodings.aliases', 
'encodings', 'encodings.utf_8', '_signal', '_abc', 'abc', 'io', '__main__', '_stat', 'stat', '_collections_abc', 'genericpath', 'posixpath', 'os.path', 'os', '_sitebuiltins', '_distutils_hack', 'types', 'importlib._bootstrap', 
'importlib._bootstrap_external', 'warnings', 'importlib', 'importlib._abc', 'itertools', 'keyword', '_operator', 'operator', 'reprlib', '_collections', 'collections', '_functools', 'functools', 'contextlib', '_weakrefset', 'threading', 
'importlib.util', 'importlib.machinery', 'google', 'site', 'groupinfo', 'settings', 'settings.constants', 'settings.variables', 'helpers', 'math', 'helpers.helpers', 'static', 'static.baseload', 'static.pv', 'static.windturbine', 'weakref', 
'copyreg', 'copy', 'ev', 'ev.evsim', '_bisect', 'bisect', '_random', '_sha512', 'random', 'ev.evgreedy', 'ev.evprices', 'ev.evco2', 'ev.evself', 'ev.evflat', 'static.ev', 'battery', 'battery.batterysim', 'battery.batterygreedy', 
'battery.batteryprices', 'battery.batteryco2', 'battery.batteryself', 'battery.batteryflat', 'static.battery', 'static.house', 'encodings.utf_8_sig', 'settings.variables_validation', 'enum', '_sre', 're._constants', 're._parser', 
're._casefix', 're._compiler', 're', 'fnmatch', 'errno', 'zlib', '_compression', '_bz2', 'bz2', '_lzma', 'lzma', 'shutil', '_locale', 'locale', 'signal', 'fcntl', '_posixsubprocess', 'select', 'collections.abc', 'selectors', 'subprocess', 
'python_temp', 'python_temp.groupinfo', 'simulator', 'mpl_toolkits', 'repoze', 'apport_python_hook', 'sitecustomize', 'nt', 'winreg', 'encodings.cp1252', '_winapi', 'ntpath', 'pywin32_system32', 'pywin32_bootstrap', 'encodings.latin_1', '_bootlocale', '_heapq', 'heapq']


# denied modules:
cfg_sim['mod_denylist']     = ['numpy', 'scipy', 'pandas', 'optAlg', 'pyomo', 'cvxpy']


# Cost parameters for verification
cfg_sim['ver_allowed_cost_bat'] =   {   0: -1.5,
                                        1: -1.5
                                    }
