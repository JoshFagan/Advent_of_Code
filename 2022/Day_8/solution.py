#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = np.array([ [int(c) for c in row[0]] for row in reader])
    return data


def process_data(raw_data):
    return raw_data 


def is_visable(input_list):
    is_vis     = np.zeros(input_list.shape)
    max_matrix = np.zeros(input_list.shape)

    is_vis[0]     = 1
    max_matrix[0] = input_list[0]

    for i in range(1, len(max_matrix)):
        max_matrix[i] = max(input_list[i], max_matrix[i-1])
        is_vis[i] = int(max_matrix[i-1]<input_list[i])

def num_visable(grid):
    (row, col) = grid.shape
    vis = np.empty((4, row, col))

    for i in range(4):
        for i in range(len(grid) 
            vis[i




def first_half(puzzle_input): 
    num_visable(puzzle_input)

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
    raw_data = load_data() 
    data = process_data(raw_data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
