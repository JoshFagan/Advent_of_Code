#!python

import csv
import numpy as np


def load_data():
    # Read contents of file
    stacks = []
    moves = []
    with open('data.txt', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                if row[0].__contains__('['):
                    stacks.append(row[0])

                if row[0].__contains__('move'):
                    moves.append(row[0])
                    
    return stacks, moves


def process_data(raw_data):
    stacks = []
    moves  = []
    for stack in raw_data[0]: 
        while stack.__contains__('    '):
            stack = stack.replace(']    ', '] []')
            stack = stack.replace('    [', '[] [')
        stack = stack[1:-1]
        stack = stack.split('] [')
        stacks.append(stack)

    for move in raw_data[1]:
        move = move.replace('move ', '')
        move = move.replace(' from ', ',')
        move = move.replace(' to ', ',')
        move = move.split(',')
        moves.append(move)
    
    return stacks, moves 


def first_half(puzzle_input): 
    init_stacks = puzzle_input[0]
    moves = puzzle_input[1]
    stacks = init_stacks[0]

    for stack in init_stacks[1:]:
        for i in range(len(stack)):
            stacks[i] += stack[i]

    for move in moves:
        num = int(move[0])
        src = int(move[1])-1
        des = int(move[2])-1
        stacks[des] = stacks[src][0:num][::-1] + stacks[des]
        stacks[src] = stacks[src][num:]

    solution = ''.join([stack[0] for stack in stacks]) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(puzzle_input):
    init_stacks = puzzle_input[0]
    moves = puzzle_input[1]
    stacks = init_stacks[0]

    for stack in init_stacks[1:]:
        for i in range(len(stack)):
            stacks[i] += stack[i]

    for move in moves:
        num = int(move[0])
        src = int(move[1])-1
        des = int(move[2])-1
        stacks[des] = stacks[src][0:num] + stacks[des]
        stacks[src] = stacks[src][num:]

    solution = ''.join([stack[0] for stack in stacks]) 
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    data = process_data(data)
    first_half(data)
    data = load_data() 
    data = process_data(data)
    second_half(data)


if __name__ == '__main__':
    main()
