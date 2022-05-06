#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

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
    # Create graph
    max_row = max(max(start_poses[:,1]), 
                max(end_poses[:,1]))
    max_col = max(max(start_poses[:,0]), 
                max(end_poses[:,0]))
    graph = np.zeros((max_row+1, max_col+1))

    # Add all lines to graph
    for i in range(len(start_poses)):
        row_a = start_poses[i,1]
        row_b = end_poses[i,1]
        col_a = start_poses[i,0]
        col_b = end_poses[i,0]
        # Only add lines that are horizontal or vertical
        if row_a != row_b and col_a != col_b: 
           continue

        # Iterate over every row
        for row in range(min(row_a, row_b), max(row_a, row_b)+1):
            # Iterate over every column
            for col in range(min(col_a, col_b), max(col_a, col_b)+1):
                # Increment every element on line
                graph[row][col] += 1

    solution = sum(sum(graph>=2))
    print('\nSolution for first half!')
    print('Number of \"2 or higher\" locations: {}\n'.format(solution))
    return graph
        

def second_half(start_poses, end_poses, graph):
    # Add all lines to graph
    for i in range(len(start_poses)):
        row_a = start_poses[i,1]
        row_b = end_poses[i,1]
        col_a = start_poses[i,0]
        col_b = end_poses[i,0]
        # Only add lines that are diagonal with angle 45 
        if col_a == col_b:
            continue
        if abs(row_b-row_a) / abs(col_b-col_a) != 1: 
            continue

        # Determine sign of slope of line
        sign_row = int((row_b-row_a)/abs(row_b-row_a))
        sign_col = int((col_b-col_a)/abs(col_b-col_a))

        # Iterate over row and column simultaneously and increment graph
        row = row_a
        for col in range(col_a, col_b+sign_col, sign_col):
            graph[row][col] += 1
            row += sign_row

    solution = sum(sum(graph>=2))
    print('\nSolution for first half!')
    print('Number of \"2 or higher\" locations: {}\n'.format(solution))
    return


def main():
    vents = load_data() 
    start_poses, end_poses = process_data(vents)
    graph = first_half(start_poses, end_poses)
    second_half(start_poses, end_poses, graph)


if __name__ == '__main__':
    main()
