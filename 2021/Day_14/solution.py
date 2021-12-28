#!/usr/bin/python

import csv


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=' ')
        data = [[value for value in row] for row in data]
    return data


def process_data(raw_data):
    rules = {}
    template = raw_data[0][0]

    for rule in raw_data[2:]:
        rules[rule[0]] = rule[2]

    return rules, template 


def get_letter_counts(poly_counts):
    letter_counts = {}
    for poly in poly_counts:
        try:
            letter_counts[poly[0]] += poly_counts[poly] 
        except:
            letter_counts[poly[0]] = poly_counts[poly] 
        try:
            letter_counts[poly[1]] += poly_counts[poly] 
        except:
            letter_counts[poly[1]] = poly_counts[poly] 

    return letter_counts 


def first_half(num_step, rules, template): 
    print(template)
    polymer = list(template)

    for step in range(num_step):
        for i in range(len(polymer)-1,0,-1):
            rule = polymer[i-1]+polymer[i]
            try:
                polymer.insert(i, rules[rule])
            except:
                pass


    



def first_half_dict(num_step, rules, template): 
    poly_counts = {}
    for i in range(len(template)-1):
        poly = template[i:i+2]
        try:
            poly_counts[poly] += 1
        except:
            poly_counts[poly] = 1

    for step in range(num_step):
        new_poly_count = poly_counts.copy()
        for rule in rules:
            try:
                num_poly = poly_counts[rule]
            except:
                continue

            # Subtract number of old pair
            new_poly_count[rule] -= num_poly
            # Add number of left pair
            try:
                new_poly_count[rule[0]+rules[rule]] += num_poly
            except:
                new_poly_count[rule[0]+rules[rule]] = num_poly
            # Add number of right pair
            try:
                new_poly_count[rules[rule]+rule[1]] += num_poly
            except:
                new_poly_count[rules[rule]+rule[1]] = num_poly

        poly_counts = new_poly_count 

    letter_counts = get_letter_counts(poly_counts)
    print(letter_counts)

    least_common = min(letter_counts.values())
    most_common = max(letter_counts.values())

    solution = most_common - least_common 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(input):
    solution = 'NOT DONE YET' 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    rules, template = process_data(data)
    first_half(10, rules, template)
    second_half(data)


if __name__ == '__main__':
    main()
