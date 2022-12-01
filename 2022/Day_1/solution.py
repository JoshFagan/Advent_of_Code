#!python

import csv
import numpy as np


def load_data():
    # Read contents of file
    data = []
    elf = []
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                elf.append(int(row[0]))
            else:
                data.append(elf)
                elf = []
        data.append(elf)
    return data


def process_data(raw_data):
    return 


def first_half(input): 
    total_cals = [sum(cals) for cals in input]
    solution = max(total_cals) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    total_cals = [sum(cals) for cals in input]
    total_cals.sort()
    solution = sum(total_cals[-3:])
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
