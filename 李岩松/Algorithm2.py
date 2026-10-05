# This algorithm is called BtLineSearch.
# Initiate with eta=eta_max.If it satisfies Armijo condition, then end and return eta. 
# If not, repeat changing eta until satisfing the condition or eta < eta_min.
# If it's the latter one, then eta=0.
import numpy as np