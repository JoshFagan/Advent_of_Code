#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


class Packet():
    def __init__(self):
        self.type_id = 0# literal or operator
        self.length_type_id = 0 # 0 - total length in bits, 
                                # 1 - number of sub-packets contained
        self.num_sub_packs = 0 # Not used if length type ID equals 0
        self.total_length = 0 # Not used if length type ID equals 1
        self.sub_packs = []


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile) 
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    return 


def first_half(transmissions):
    p = Packet()
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
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
