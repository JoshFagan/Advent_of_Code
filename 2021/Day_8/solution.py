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
    signals = np.array([[set(i) for i in r.split('|')[0].split()] 
                        for r in raw_data]) 
    outputs = np.array([[set(i) for i in r.split('|')[1].split()] 
                        for r in raw_data]) 
    return signals, outputs 


def first_half(outputs): 
    # In the output values, how many times do digits 1, 4, 7, or 8 appear?
    # digit: length
    # 1: 2
    # 4: 4
    # 7: 3
    # 8: 7
    solution = sum(map(lambda entry: 
                        sum([len(x) <= 4 or len(x) == 7 for x in entry]), 
                        outputs))

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def subtract_digits(entry, digit):
    return np.array([len(x-digit) for x in entry])

    
def second_half(signals, outputs):
    solution = 0
    for i in range(len(signals)):
        signal = signals[i]
        conns = {}
        # Get original lengths of encodings 
        len_og = subtract_digits(signal, set(''))
        # Add conns for unique lengths
        conns['1'] = signal[len_og==2][0] 
        conns['4'] = signal[len_og==4][0] 
        conns['7'] = signal[len_og==3][0] 
        conns['8'] = signal[len_og==7][0] 

        # Remove conns we know 
        signal = remove_known_conns(signal, len_og, [2, 4, 3, 7])

        # Remove conns we know belong to 1 digit 
        len_less_one = subtract_digits(signal, conns['1'])
        # Add conns for unique lengths
        conns['3'] = signal[len_less_one==3][0] 
        conns['6'] = signal[len_less_one==5][0] 

        # Remove conns we know 
        signal = remove_known_conns(signal, len_less_one, [3, 5])

        # Remove conns we know belong to 1 and 4
        len_less_four = subtract_digits(signal, conns['1'].union(conns['4']))
        # Add conns for unique lengths
        conns['0'] = signal[(len_og==6) & (len_less_four==3)][0]   
        conns['2'] = signal[(len_og==5) & (len_less_four==3)][0]   
        conns['5'] = signal[(len_og==5) & (len_less_four==2)][0]   
        conns['9'] = signal[(len_og==6) & (len_less_four==2)][0]   
    
        # Index dictionary of conns from value
        value_list = list(conns.values())
        key_list   = list(conns.keys())
        string_digit = ''

        # Add up strings of digits
        for o in range(4):
            string_digit += key_list[value_list.index(outputs[i][o])]

        solution += int(string_digit)

    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    signals, outputs = process_data(data)
    first_half(outputs)
    second_half(signals, outputs)


if __name__ == '__main__':
    main()
