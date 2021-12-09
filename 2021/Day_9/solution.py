#!/usr/bin/python3.8

import numpy as np
import scipy
from scipy import stats


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def process_data(raw_data):
    data = np.array([[int(c) for c in row.strip()] for row in raw_data])
    return data 



def first_half(map): 
    solution = 0
    num_row, num_col = map.shape
    for row in range(num_row):
        for col in range(num_col):
            neighbors = np.array([])
            for offset in [-1, 1]:
                if row+offset >= 0 and row+offset < num_row: 
                    neighbors = np.append(neighbors, map[row+offset][col])

                if col+offset >= 0 and col+offset < num_col: 
                    neighbors = np.append(neighbors, map[row][col+offset])

            if map[row][col] < np.amin(neighbors):
                solution += (1+map[row][col]) 

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    data = process_data(data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
