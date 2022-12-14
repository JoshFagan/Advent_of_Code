#!python

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
    max_matrix = np.zeros(input_list.shape)
    max_matrix[0] = input_list[0]
    for i in range(1, len(max_matrix)):
        max_matrix[i] = max(input_list[i], max_matrix[i-1])

    print(input_list)
    print(max_matrix)



def first_half(puzzle_input): 
    rolling_max(puzzle_input[0])

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
