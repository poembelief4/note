# This algorithm is called gradient compensation algorithm. It can compute the next x in gradient decent.
# First, check whether the backtracking line search succeeds. 
# If yes, return the new value using old function. 
# If not, update step size and the function.then return the new value.
import numpy as np