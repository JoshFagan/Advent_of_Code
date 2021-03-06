#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np 


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    coords = set([]) 
    folds = []
    for row in raw_data:
        if len(row) == 2:
            coords.add((int(row[0]), int(row[1])))
        elif len(row) == 1:
            parsed = row[0].split('=')
            folds.append((int(parsed[0][-1]=='y'), int(parsed[1])))

    return coords, folds 


def first_half(coords, folds): 
    fold = folds[0]
    new_coords = set([]) 
    for coord in coords:
        if fold[0] == 1:
            new_x = coord[0]
            new_y = min(coord[1], 2*fold[1]-coord[1])
        if fold[0] == 0:
            new_x = min(coord[0], 2*fold[1]-coord[0])
            new_y = coord[1]

        new_coords.add((new_x, new_y))
    coords = new_coords

    solution = len(coords) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(coords, folds):
    for fold in folds:
        new_coords = set([]) 
        for coord in coords:
            if fold[0] == 1:
                new_x = coord[0]
                new_y = min(coord[1], 2*fold[1]-coord[1])
            if fold[0] == 0:
                new_x = min(coord[0], 2*fold[1]-coord[0])
                new_y = coord[1]
    
            new_coords.add((new_x, new_y))
        coords = new_coords

    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])

    display = np.zeros((max_y+1, max_x+1))

    for coord in coords:
        display[coord[1],coord[0]] = 1

    with open('display.txt', mode='w') as file_object:
        print(display, file=file_object)


    solution = len(coords) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    coords, folds = process_data(data)
    first_half(coords, folds)
    second_half(coords, folds)


if __name__ == '__main__':
    main()
