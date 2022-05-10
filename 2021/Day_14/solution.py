#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        data = [[value for value in row] for row in data]
    return data


def process_data(raw_data):
    poly = raw_data[0][0]
    rules = {}
    pair_count = {}
    sing_count = {}

    for rule in raw_data[2:]:
        rules[rule[0]] = rule[2]

    for i in range(len(poly)-1):
        pair_count[poly[i:i+2]] = pair_count.get(poly[i:i+2], 0) + 1
        sing_count[poly[i]] = sing_count.get(poly[i], 0) + 1

    sing_count[poly[-1]] = sing_count.get(poly[-1], 0) + 1

    return poly, rules, sing_count, pair_count


def first_half(rules, s_count, p_count, num_step):
    for step in range(num_step):
        p_count = insertion_step(rules, s_count, p_count)

    solution = max(s_count.values()) - min(s_count.values()) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 


def insertion_step(rules, s_count, p_count):
    new_p_count = {}
    for (p, count) in p_count.items():
        new_e = rules[p]
        # Add count for new letter being added
        s_count[new_e] = s_count.get(new_e, 0) + count
        # Increment two new pair counts
        new_p_count[p[0]+new_e] = new_p_count.get(p[0]+new_e, 0) + count 
        new_p_count[new_e+p[1]] = new_p_count.get(new_e+p[1], 0) + count

    return new_p_count
        

def second_half(rules, s_count, p_count, num_step):
    for step in range(num_step):
        p_count = insertion_step(rules, s_count, p_count)

    solution = max(s_count.values()) - min(s_count.values()) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    poly, rules, s_count, p_count = process_data(data)
    first_half(rules, s_count, p_count, 10) 
    poly, rules, s_count, p_count = process_data(data)
    second_half(rules, s_count, p_count, 40) 


if __name__ == '__main__':
    main()
