#!/usr/bin/python

import numpy
import scipy
from scipy import stats


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def process_data(raw_data):
    clean_data = [[int(char) for char in row[:-1]] for row in raw_data]
    return clean_data


def first_half(report): 
    (gamma, _)= stats.mode(report, axis=1)

    print('\nSolution for first half!')
    print('Product of depth and horizontal position: {}\n'.format(solution))


def second_half(report):
    print('Solution for second half!')
    print('Product of depth and horizontal position: {}\n'.format(solution))


def main():
    report = load_data() 
    report = process_data(report)
    first_half(report)
#    second_half(report)


if __name__ == '__main__':
    main()
