#!python

import csv
import numpy as np


class Directory:
    def __init__(self, name, parent, indent_string):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []
        self.indent_string = indent_string
        self.size = 0

    def __str__(self):
        file_structure = "{}- {} (dir, size={})\n".format(self.indent_string,
                                                          self.name,
                                                          self.size)
        for child in self.children:
            file_structure += f"{child}"

        for file in self.files:
            file_structure += f"{file}"

        return file_structure


    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
    
        new_child = Directory(name=child_name, 
                              parent=self, 
                              indent_string=self.indent_string+'  ')
        self.children.append(new_child)
    
        return new_child


    def add_file(self, file_name, file_size):
        for file in self.files:
            if file.name == file_name:
                return
                
        new_file = File(name=file_name, 
                        size=file_size, 
                        indent_string=self.indent_string+'  ')
        self.files.append(new_file)
        self.update_size()
        return


    def update_size(self):
        self.size = sum([file.size for file in self.files] +  
                        [child.size for child in self.children])

        if self.parent:
            self.parent.update_size()


class File:
    def __init__(self, name, size, indent_string):
        self.name = name
        self.size = size
        self.indent_string = indent_string

    def __str__(self):
        return "{}- {} (file, size={})\n".format(self.indent_string,
                                                 self.name,
                                                 self.size)

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
    curr_dir = root
    for command in puzzle_input[1:]:
        command = command.split(' ')
        if command[1] == 'cd':
            if command[-1] == '..':
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.get_child(command[-1])
        elif command[0].isnumeric():
            curr_dir.add_file(command[1], int(command[0]))
        
    return root


def get_dir_sizes(curr_dir):
    dir_sizes = []
    dir_sizes.append(curr_dir.size)

    for child in curr_dir.children:
        dir_sizes += get_dir_sizes(child)

    return dir_sizes 


def first_half(root): 
    dir_sizes = get_dir_sizes(root) 
    solution = sum([size for size in dir_sizes if size <= 100000])
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(root):
    total_space = 70000000
    needed_space = 30000000
    used_space = root.size
    free_space = total_space-used_space
    extra_needed_space = needed_space - free_space

    if extra_needed_space > 0:
        dir_sizes = get_dir_sizes(root)
        candidate_dir = min([size for size in dir_sizes 
                             if size >= extra_needed_space])

    solution = candidate_dir 
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    raw_data = load_data() 
    root = create_file_system(raw_data)
    print(root)
    first_half(root)
    second_half(root)


if __name__ == '__main__':
    main()
