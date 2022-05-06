#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

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
    data = np.array([[int(octo) for octo in row.strip()] for row in raw_data])
    return data


def first_half_recurssion(octopi, row, col):
    # Check to make sure indices are within bounds
    num_row, num_col = octopi.shape
    if row <= -1 or row >= num_row or col <= -1 or col >= num_row:
        return 

    # Skip if octopus has already been activated
    if octopi[row][col] == 0:
        return

    # Update octopus' value
    octopi[row][col] += 1

    # If octopus is activated, update neighbors
    if octopi[row][col] >= 10:
        octopi[row][col] = 0   # Mark octopus as activated
        for r in range(-1, 2):
            for c in range(-1, 2):
                first_half_recurssion(octopi, row+r, col+c)


def first_half(octopi): 
    solution = 0
    for step in range(100):
        octopi += 1
        rows, cols = np.where(octopi==10)
        for i in range(len(rows)):
            first_half_recurssion(octopi, rows[i], cols[i])

        solution += sum(sum(octopi == 0))
            
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(octopi):
    solution = 0

    while 1:
        solution += 1
        octopi += 1
        rows, cols = np.where(octopi==10)
        for i in range(len(rows)):
            first_half_recurssion(octopi, rows[i], cols[i])

        if sum(sum(octopi)) == 0:
            break

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    data = process_data(data)
    first_half(np.copy(data))
    second_half(np.copy(data))


if __name__ == '__main__':
    main()
