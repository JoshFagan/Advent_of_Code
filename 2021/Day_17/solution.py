#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import time

import csv
import numpy as np


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='<DELIMITER>')
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    return 


def calc_trajectory_1(x_vel, y_vel, time_steps):
    x = [0]
    y = [0]

    for i in range(time_steps):
        x.append(x[i]+x_vel)
        y.append(y[i]+y_vel)
        x_vel = max(x_vel-1, 0)
        y_vel -= 1


def calc_trajectory_2(x_vel, y_vel, time_steps):
    x = np.array(range(x_vel, x_vel-time_steps, -1))
    x[x<0] = 0
    x = np.cumsum(x)
    y = np.cumsum(range(y_vel, y_vel-time_steps, -1))


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
#    data = load_data() 
#    process_data(data)
#    first_half(data)
#    second_half(data)

    t1 = time.time()
    calc_trajectory_2(7, 2, 100000)
    t2 = time.time()

    calc_trajectory_1(7, 2, 100000)
    t3 = time.time()

    print(t2-t1)
    print(t3-t2)


if __name__ == '__main__':
    main()
