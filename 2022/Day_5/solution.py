#!python

import csv
import numpy as np


def load_data():
    # Read contents of file
    stacks = []
    moves = []
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                if row[0].__contains__('['):
                    r = row[0]
                    r = r.replace(']    ', '] []')
                    r = r.replace('    [', '[] [')
                    r = r[1:-1]
                    r = r.split('] [')
                    stacks.append(r)

                if row[0].__contains__('move'):
                    moves.append(row[0])
                    
    return stacks, moves


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
    print(data)
    process_data(data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
