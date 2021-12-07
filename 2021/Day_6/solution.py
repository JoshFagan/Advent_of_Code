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
    initial_state = [int(f) for f in raw_data[0].split(',')]
    return initial_state 


def solution(initial_state, days): 
    # Initialize empty counts
    fish_count = {-1:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    # Propogate counts with intitial state
    for fish in initial_state:
        fish_count[fish] = fish_count[fish] + 1

    # Each Day
    for day in range(days):
        # Roll each fish count down one
        for fish in range(9):
            fish_count[fish-1] = fish_count[fish]
        # Adjust for resetting fish
        fish_count[6] += fish_count[-1]
        fish_count[8] = fish_count[-1]
            

    fish_count[-1] = 0
    solution = sum(fish_count.values())
    print('\nSolution!')
    print('How many lanternfish after {} days?: {}\n'.format(days, solution))
    return 
        

def main():
    data = load_data() 
    initial_state = process_data(data)
    solution(initial_state, 80)
    solution(initial_state, 256)


if __name__ == '__main__':
    main()
