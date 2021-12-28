#!/usr/bin/python3.8

import csv


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='<DELIMITER>')
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    return 


def first_half(input): 
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
    process_data(data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
