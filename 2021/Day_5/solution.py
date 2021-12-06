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
    coordinates = [line.split() for line in raw_data]
    start_poses = np.array([c[0].split(',') for c in coordinates], dtype=int)
    end_poses = np.array([c[2].split(',') for c in coordinates], dtype=int)
    return start_poses, end_poses


def first_half(start_poses, end_poses): 
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('Number of \"2 or higher\" locations: {}\n'.format(solution))
    return
        

def second_half(start_poses, end_poses):
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('Number of \"2 or higher\" locations: {}\n'.format(solution))
    return


def main():
    vents = load_data() 
    start_poses, end_poses = process_data(vents)
    first_half(start_poses, end_poses)
    second_half(start_poses, end_poses)


if __name__ == '__main__':
    main()
