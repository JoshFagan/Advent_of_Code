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
    data = np.array([[int(c) for c in row.strip()] for row in raw_data])
    return data 


def first_half(map): 
    low_points = [] 
    solution = 0
    num_row, num_col = map.shape
    for row in range(num_row):
        for col in range(num_col):
            neighbors = np.array([])
            for offset in [-1, 1]:
                if row+offset >= 0 and row+offset < num_row: 
                    neighbors = np.append(neighbors, map[row+offset][col])

                if col+offset >= 0 and col+offset < num_col: 
                    neighbors = np.append(neighbors, map[row][col+offset])

            if map[row][col] < np.amin(neighbors):
                solution += (1+map[row][col]) 
                low_points.append([row,col])

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return low_points 


def second_half_recusion(map, row, col):
    num_row, num_col = map.shape
    # If given point is out of bounds, do not count point
    if row < 0 or row >= num_row or col < 0 or col >= num_col:
        return 0, map

    # If given point has already been counted, or is a peak, do not count point
    if not map[row][col]:
        return 0, map

    # Indicate point as being counted
    map[row][col] = 0

    num_c = 0
    # Return one plus all connecting points
    for offset in [-1, 1]:
        num_cr, map = second_half_recusion(map, row+offset, col) 
        num_cc, map = second_half_recusion(map, row, col+offset) 
        num_c += (num_cr + num_cc)

    return num_c + 1, map
        

def second_half(map, low_points):
    free_points = map!=9
    basin_sizes = []
    for point in low_points:
        basin_size, _ = second_half_recusion(free_points, point[0], point[1])
        basin_sizes.append(basin_size)
    
    basin_sizes.sort()
    solution = np.prod(basin_sizes[-3:]) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    data = process_data(data)
    low_points = first_half(data)
    second_half(data, low_points)


if __name__ == '__main__':
    main()
