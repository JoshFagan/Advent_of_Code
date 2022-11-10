#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='\n')
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    return 


def first_half(input): 
    # An opening parenthesis, (, means he should go up one floor, and a 
    # closing parenthesis, ), means he should go down one floor.
    # The apartment building is very tall, and the basement is very deep; he 
    # will never find the top or bottom floors.
    # To what floor do the instructions take Santa?

    solution = len(input)-(2*input.count(')')) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    solution = 0
    floor = 0
    while 0 <= floor:
        floor += 1 if input[solution] == '(' else -1
        solution += 1

    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    for d in data:
        first_half(d[0])
    for d in data:
        second_half(d[0])


if __name__ == '__main__':
    main()
