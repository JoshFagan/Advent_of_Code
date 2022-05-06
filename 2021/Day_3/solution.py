#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import numpy
import scipy
from scipy import stats


def load_data():
    # Read contents of file
    my_file = open('data.txt', 'r')
    contents = my_file.readlines()
    my_file.close()

    return contents 


def process_data(raw_data):
    clean_data = [[int(char) for char in row[:-1]] for row in raw_data]
    return clean_data


def first_half(report): 
    # Use the binary numbers in the diagnostic report to generate two new 
    # binary numbers (gamma rate and epsilon rate). 
    # The power consumption can then be found by multiplying the gamma rate by 
    # the epsilon rate.

    # Gamma rate is the most common bit in the corresponding position of all 
    # numbers in the diagnostic report
    (gamma, _)= stats.mode(report, axis=0)
    # Epsilon rate is the least common bit in the corresponding position of all 
    # numbers in the diagnostic report
    epsilon = [(g+1) % 2 for g in gamma]

    # Multiplying the gamma rate by the epsilon rate gives the power consumption
    gamma = int(''.join([str(g) for g in gamma[0]]), 2)
    epsilon = int(''.join([str(e) for e in epsilon[0]]), 2)

    solution = gamma * epsilon 

    print('\nSolution for first half!')
    print('Product of gamma and epsilon: {}\n'.format(solution))


def second_half_recursion(report, bit, use_most_freq):
    (most_freq, count) = stats.mode([entry[bit] for entry in report], axis=0)

    # If 0 and 1 are equally common, use special rules
    if count == len(report) / 2:
        most_freq = 1

    filtered = [entry for entry in report 
                if (entry[bit] == most_freq) == use_most_freq]

    if len(filtered) == 1:
        return filtered
    else:
        return second_half_recursion(filtered, bit+1, use_most_freq)
        


def second_half(report):
    # Verify the life support rating, which can be determined by multiplying 
    # the oxygen generator rating by the CO2 scrubber rating
    oxygen_rating = second_half_recursion(report, 0, 1)
    co2_rating = second_half_recursion(report, 0, 0)

    oxygen_rating = int(''.join([str(o) for o in oxygen_rating[0]]), 2)
    co2_rating = int(''.join([str(c) for c in co2_rating[0]]), 2)

    # Finally, to find the life support rating, multiply the oxygen generator 
    # rating by the CO2 scrubber rating
    solution = oxygen_rating * co2_rating

    print('Solution for second half!')
    print('Product of oxygen rating and co2 rating: {}\n'.format(solution))


def main():
    report = load_data() 
    report = process_data(report)
    first_half(report)
    second_half(report)


if __name__ == '__main__':
    main()
