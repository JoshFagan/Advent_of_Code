#!python

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [row[0] for row in reader]
    return data


def process_data(raw_data):
    return 


def first_half(puzzle_input): 
    solution = 'NOT DONE YET' 
    for i in range(len(puzzle_input)-3):
        if len(set(puzzle_input[i:i+4])) == 4:
            solution = i + 4
            break
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(puzzle_input):
    solution = 'NOT DONE YET' 
    for i in range(len(puzzle_input)-13):
        if len(set(puzzle_input[i:i+14])) == 14:
            solution = i + 14
            break
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    process_data(data)
    first_half(data[0])
    second_half(data[0])


if __name__ == '__main__':
    main()
