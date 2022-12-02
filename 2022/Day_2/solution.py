#!python

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        data = np.array([[value for value in row] for row in data])
    return data


def first_half(input):
    mapping = {'A': {'X': 4, 'Y': 8, 'Z': 3}, 
               'B': {'X': 1, 'Y': 5, 'Z': 9},
               'C': {'X': 7, 'Y': 2, 'Z': 6}}

    scores = [mapping[i[0]][i[1]] for i in input]
    solution = sum(scores) 

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    mapping = {'A': {'X':3 , 'Y': 4, 'Z': 8}, 
               'B': {'X':1 , 'Y': 5, 'Z': 9},
               'C': {'X':2 , 'Y': 6, 'Z': 7}}

    scores = [mapping[i[0]][i[1]] for i in input]
    solution = sum(scores) 
    
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
