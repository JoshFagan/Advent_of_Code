#!/usr/bin/python

import pandas as pd


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def first_half(course):
    print('\nSolution for first half!')
    print('Product of depth and horizontal position: {}\n'.format(solution))


def second_half(course):
    print('Solution for second half!')
    print('Product of depth and horizontal position: {}\n'.format(solution))


def main():
    report = load_data() 
#    first_half(report)
    second_half(report)


if __name__ == '__main__':
    main()
