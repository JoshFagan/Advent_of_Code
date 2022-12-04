#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile)
        data = np.array([row[0] for row in data])
    return data


def split_compartments(raw_data):
    data = [[sack[0:len(sack)//2], sack[len(sack)//2:]] for sack in raw_data]
    return data


def make_groups(raw_data):
    data = [[raw_data[i-2], raw_data[i-1], raw_data[i]] 
            for i in range(2, len(raw_data), 3)]
    return data


def get_duplicate(compartments):
    return [item for item in compartments[0] if item in compartments[1]]


def get_badge(elf):
    for item in elf[0]:
        if item in elf[1] and item in elf[2]:
            return item 


def get_priority(item):
    return ord(item)-96 if item.islower() else ord(item)-38


def first_half(input): 
    input = split_compartments(input)
    error_items = [get_duplicate(sack) for sack in input]
    solution = sum([get_priority(item[0]) for item in error_items])
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    groups = make_groups(input)
    badges = [get_badge(group) for group in groups]
    solution = sum([get_priority(item) for item in badges])
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
