#!/usr/bin/python3.8

import numpy as np
import scipy
from scipy import stats


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def process_data(raw_data):
    return ([], [])


def first_half(draw_numbers, boards): 
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('Number of \"2 or higher\" locations: {}\n'.format(solution))
    return
        

def second_half(draw_numbers, boards):
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('Number of \"2 or higher\" locations: {}\n'.format(solution))
    return


def main():
    vents = load_data() 
    (start_pos, end_pos) = process_data(vents)
    first_half(start_pos, end_pos)
    second_half(start_pos, end_pos)


if __name__ == '__main__':
    main()
