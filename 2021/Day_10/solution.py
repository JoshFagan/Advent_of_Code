#!/Users/josh/opt/anaconda3/bin/python

#import numpy as np
#import scipy
#from scipy import stats


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def process_data(raw_data):
    data = [[char for char in row.strip()] for row in raw_data]
    return data 


def score_line(line):
    matches = {')':'(', ']':'[', '}':'{', '>':'<'}
    scores  = {')':3, ']':57, '}':1197, '>':25137}
    stack   = []

    for pair_char in line:
        if pair_char in matches:
            match = stack.pop()
            if match != matches[pair_char]:
                return scores[pair_char], [] 
        else:
            stack.append(pair_char)
    return 0, stack 


def first_half(nav_msgs): 
    solution = 0
    
    incomplete = []

    for line in nav_msgs:
        score, rem_line = score_line(line)
        if score == 0:
            incomplete.append(rem_line)
        solution += score 

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return incomplete 


def score_incomplete(line):
    points = {'(':1, '[':2, '{':3, '<':4}
    score  = 0

    line.reverse()
    for pair_char in line:
        score *= 5
        score += points[pair_char]

    return score
        

def second_half(incomplete):
    # Find the completion string for each incomplete line
    # score the completion strings, 
    scores = []
    for line in incomplete:
        scores.append(score_incomplete(line))
    # Sort the scores. What is the middle score?
    scores.sort()
    solution = scores[int(len(scores)/2)]
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    data = process_data(data)
    incomplete = first_half(data)
    second_half(incomplete)


if __name__ == '__main__':
    main()
