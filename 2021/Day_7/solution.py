#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import numpy as np
import scipy
from scipy import stats
import csv
from scipy.optimize import minimize
from math import ceil


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data = np.array([int(height) for row in data for height in row])
    return data 


def first_half(heights): 
    fun = lambda x: sum(abs(x - heights))
    res = minimize(fun,5) 
    min_height = round(res.x[0])
    solution = int(round(fun(min_height)))
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(heights):
    fun = lambda x: sum((abs(x-heights)*(abs(x-heights)+1))/2)
    res = minimize(fun,2) 
    min_height = round(res.x[0])
    solution = int(round(fun(min_height)))
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
