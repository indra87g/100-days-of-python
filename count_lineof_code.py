""" 
Simple math operation to count line of code that i written in 100 Days of Python :D
How it works?
Pretty simple, this script will count Mean an Total of array 'lineof_code' with 'numpy'
"""
import numpy as np

# Line of code. including all python code from day 1 - 100
lineof_code = np.array([[
    35, 31, 98, 20, 142, 38, 60, 47, 83, 53, 43, 61,
    52, 58, 82, 37, 120, 93, 36, 30, 36, 35, 60, 26,
    47, 88, 22, 5, 115, 54, 60, 53, 71
]])

print(f"Mean: {np.mean(lineof_code)}")
print(f"Total: {np.sum(lineof_code)}")
