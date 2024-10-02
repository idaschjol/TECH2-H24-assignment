"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt
import numpy as np


def std_loops(x):
    N = len(num_lst)
    mean = 0
    for num in num_lst:
        mean += num
    mean /= N
    
    
    variance = 0
    for num in num_lst:
        variance += (num-mean)**2
    variance /= N
    
    
    std = sqrt(variance)
    return std
    
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
      

def std_builtin(x):
    N = len(num_lst)
    mean = sum(num_lst)/N
    variance = sum((x-mean)**2 for x in num_lst)/N 
    std = sqrt(variance)
    return std


    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
   
def std_numpy(num_lst):
    return np.std(num_lst)


num_lst = [1, 2, 3, 4, 5]

std1 = std_loops(num_lst)
std2 = std_builtin(num_lst)
std3 = std_numpy(num_lst)


print(f"Standard Deviation (Loop): {std1}")
print(f"Standard Deviation (Built-in): {std2}")
print(f"Standard Deviation (NumPy): {std3}")




