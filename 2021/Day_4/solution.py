#!/usr/bin/python3.8

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
    draw_numbers = [int(x) for x in raw_data[0].split(',')]

    boards = np.array([[int(x) for x in row.split()] 
                       for row in raw_data[2:] if row if row != '\n'])

    return (draw_numbers, boards) 


def first_half(draw_numbers, boards): 
    # Set up mechanics to track scoring numbers
    num_boards = int(boards.shape[0]/5)
    row_counts = np.zeros((5, num_boards)) 
    col_counts = np.zeros((num_boards, 5))
    # Iterate over all numbers
    for num in draw_numbers:
        indices = np.where(boards==num)
        # Score all numbers
        for i in range(len(indices[0])):
            # Parse specifics about location of drawn number
            game = int(indices[0][i]/5)
            row = indices[0][i] % 5
            col = indices[1][i]

            # Mark the position on the board as drawn
            boards[indices[0][i]][indices[1][i]] = 0

            # Update drawn row and column counts
            row_counts[row][game] += 1
            col_counts[game][col] += 1

            # End game if row or column counts for a game wins
            if row_counts[row][game] >= 5 or col_counts[game][col] >= 5:
                solution = sum(sum(boards[game*5:game*5+5])) * num
                print('\nSolution for first half!')
                print('Product of board sum and drawn number: {}\n'.format(
                          solution))
                return
        

def second_half(draw_numbers, boards):
    # Set up mechanics to track scoring numbers
    num_boards = int(boards.shape[0]/5)
    row_counts = np.zeros((5, num_boards)) 
    col_counts = np.zeros((num_boards, 5))
    won_boards = np.array([])
    # Iterate over all numbers
    for num in draw_numbers:
        indices = np.where(boards==num)
        # Score all numbers
        for i in range(len(indices[0])):
            # Parse specifics about location of drawn number
            game = int(indices[0][i]/5)
            row = indices[0][i] % 5
            col = indices[1][i]
            # If this game as already one, skip updating everthing
            if game in won_boards:
                continue

            # Mark the position on the board as drawn
            boards[indices[0][i]][indices[1][i]] = -1

            # Update drawn row and column counts
            row_counts[row][game] += 1
            col_counts[game][col] += 1

            # Check if a game board wins
            if row_counts[row][game] >= 5 or col_counts[game][col] >= 5:
                # End game if this is the last game board
                if num_boards == 1:
                    # Change drawn location markers to additive identity 
                    winner = boards[game*5:game*5+5]
                    winner[winner == -1] = 0

                    solution = sum(sum(winner)) * num
                    print('\nSolution for second half!')
                    print('Product of board sum and drawn number: {}\n'.format(
                              solution))
                    return
                else:
                    # If this is not the last game, update counts and keeg going
                    won_boards = np.append(won_boards, game)
                    num_boards -= 1
                    boards[game*5:game*5+5] = -1


def main():
    bingo = load_data() 
    (draw_numbers, boards) = process_data(bingo)
    first_half(draw_numbers, boards)
    (draw_numbers, boards) = process_data(bingo)
    second_half(draw_numbers, boards)


if __name__ == '__main__':
    main()
