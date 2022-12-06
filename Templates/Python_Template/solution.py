#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='<DELIMITER>')
        data = np.array([row[0] for row in reader])
    return data


def process_data(raw_data):
    return 


def first_half(puzzle_input): 
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(puzzle_input):
    solution = 'NOT DONE YET' 
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    process_data(data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
