#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np
from itertools import combinations


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='x')
        data = np.array([[int(value) for value in row] for row in data])
    return data


def process_data(raw_data): 
    pass


def first_half(input): 
    solution = 0
    for present in input:
        sides = [side[0]*side[1] for side in combinations(present, 2)]
        solution += 2*sum(sides) + min(sides)
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    solution = 0 
    for present in input:
        sides = [side[0]+side[1] for side in combinations(present, 2)]
        solution += 2*min(sides) + np.prod(present) 
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
