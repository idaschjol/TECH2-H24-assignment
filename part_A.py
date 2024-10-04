"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt
import numpy as np


#Defining a list with the given numbers:
num_lst = [1, 2, 3, 4, 5]


def std_loops(x):
    L = len(x)  #Finding the length of the list
    mean = 0
    for num in x:  #First loop to calculate the mean
        mean += num
    mean /= L
    
    
    variance = 0
    for num in x:   #Second loop to calculate the variance
        variance += (num-mean)**2
    variance /= L
    
    
    std = sqrt(variance)  #Calcualting the standard deviation by taking the square root of the variance
    return std
    
    
    
#Doing the same by just using sum() and len()
def std_builtin(x):
    L = len(x)
    mean = sum(x)/L
    variance = sum((x-mean)**2 for x in x)/L 
    std = sqrt(variance)
    return std



#Using numpy to calculate:   
def std_numpy(x):
    return np.std(x)


#Calculating the standard deviation for all the three methods:
std1 = std_loops(num_lst)
std2 = std_builtin(num_lst)
std3 = std_numpy(num_lst)


#Printing the results:
print(f"Standard Deviation by using loops is: {std1}")
print(f"Standard Deviation by using built-in functions is: {std2}")
print(f"Standard Deviation by using NumPy is: {std3}")




