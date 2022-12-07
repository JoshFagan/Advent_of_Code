#!python

import csv
import numpy as np


class Directory:
    def __init__(self, name, parent, indent_string):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self._indent_string = indent_string

    def __str__(self):
        file_structure = f"{self._indent_string}- {self.name} (dir)\n"
        for child in self.children:
            file_structure += f"{child}"

        for file in self.files:
            file_structure += f"{file}"

        return file_structure


class File:
    def __init__(self, name, size, indent_string):
        self.name = name
        self.size = size
        self._indentation_string = indent_string

    def __str__(self):
        return f"{self._indent_string}- {self.name} (file, size={self.size})\n"

def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile) 
        data = np.array([row[0] for row in reader])

    return data


def process_data(raw_data):
    return raw_data


def create_file_system(puzzle_input):
    root = Directory(name='/', parent=None, indent_string='')
    return root


def first_half(puzzle_input): 
    root = create_file_system(puzzle_input)
    print(root)
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(puzzle_input):
    solution = 'NOT DONE YET' 
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    raw_data = load_data() 
    data = process_data(raw_data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
