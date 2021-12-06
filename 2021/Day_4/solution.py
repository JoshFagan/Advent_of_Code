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
    draw_numbers = [int(x) for x in raw_data[0].split(',')]

    boards = np.array([[int(x) for x in row.split()] for row in raw_data[2:] if row if row != '\n'])

    return (draw_numbers, boards) 


def first_half(draw_numbers, boards): 
    print(boards.shape)
    num_boards = int(boards.shape[0]/5)
    row_counts = np.zeros((5, num_boards)) 
    col_counts = np.zeros((num_boards, 5))

    print('\nSolution for first half!')
    print('Product of gamma and epsilon: {}\n'.format(solution))


def second_half(report):

    print('Solution for second half!')
    print('Product of oxygen rating and co2 rating: {}\n'.format(solution))


def main():
    bingo = load_data() 
    (draw_numbers, boards) = process_data(bingo)
    print(boards)
    first_half(draw_numbers, boards)
    second_half(bingo)


if __name__ == '__main__':
    main()
