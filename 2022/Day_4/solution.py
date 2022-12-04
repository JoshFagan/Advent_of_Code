#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    data = [[list(map(int, pair[0].split('-'))), 
             list(map(int, pair[1].split('-')))] for pair in raw_data] 
    return data


def first_half(puzzle_input): 
    overlap = [(pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or
               (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1])
               for pair in puzzle_input]
    solution = sum(overlap) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(puzzle_input):
    overlap = [(pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or
               (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0])
               for pair in puzzle_input]
    solution = sum(overlap) 
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    data = process_data(data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
