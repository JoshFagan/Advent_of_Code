#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import csv
import numpy as np


class Packet():
    def __init__(self):
        self.version = 0 
        self.type_id = 0 # literal or operator
        self.length_type_id = None # 0 - total length in bits, 
                                   # 1 - number of sub-packets contained
        self.num_sub_packs = None # Not used if length type ID equals 0
        self.total_length  = None # Not used if length type ID equals 1
        self.sub_packs = [] 
        self.value = 0 


    def parse_transmission(self, t):
        self.version = int(t[:3], 2)
        self.type_id = int(t[3:6], 2)
        t = t[6:]

        if self.type_id == 4:
            # Case when packet is a literal value
            t = self.__parse_literal_value(t)
        else:
            # Every other case is a operational packet
            t = self.__parse_operator(t)

        return t


    def __parse_literal_value(self, t):
        groups = []
        more_groups = 1
        while more_groups:
            more_groups = int(t[0]) 
            groups.append(t[1:5])
            t = t[5:]
        
        self.value = int(''.join(groups), 2)

        return t


    def __parse_operator(self, t):
        self.length_type_id = int(t[0])
        t = t[1:]

        # Need to parse out sub-packets
        if self.length_type_id:
            # Case when length type id indicates counting sub-packets 
            self.num_sub_packs = int(t[:11], 2)
            t = t[11:]
            for i in range(self.num_sub_packs):
                p = Packet()
                self.sub_packs.append(p)
                t = p.parse_transmission(t)
        else:
            # Case when length type id indicates counting total bits 
            self.total_length = int(t[:15], 2)
            t = t[15:]
            t_new = t[:self.total_length]
            t = t[self.total_length:]
            while len(t_new) > 0:
                p = Packet()
                self.sub_packs.append(p)
                t_new = p.parse_transmission(t_new)

        self.update_value()

        return t


    def update_value(self):
        sub_vals = [p.value for p in self.sub_packs]
        if self.type_id == 0: # Sum packets
            # Value is the sum of the values of their sub-packet(s) 
            self.value = sum(sub_vals)
        elif self.type_id == 1: # Product packets
            # Value is the product of the values of their sub-packet(s) 
            self.value = np.prod(sub_vals)
        elif self.type_id == 2: # Minimum packets
            # Value is the minimum of the values of their sub-packet(s)
            self.value = min(sub_vals)
        elif self.type_id == 3: # Maximum packets 
            # Value is the maximum of the values of their sub-packet(s)
            self.value = max(sub_vals)
        elif self.type_id == 5: # Greater than packets
            # Value is 1 if the value of the first sub-packet is greater than 
            # the value of the second sub-packet; otherwise, the value is 0
            # These packets always have exactly two sub-packets
            self.value = int(sub_vals[0] > sub_vals[1])
        elif self.type_id == 6: # Less than packets - 
            # Value is 1 if the value of the first sub-packet is less than 
            # the value of the second sub-packet; otherwise, the value is 0
            # These packets always have exactly two sub-packets
            self.value = int(sub_vals[0] < sub_vals[1])
        elif self.type_id == 7: # Equal to packets
            # Value is 1 if the value of the first sub-packet is equal to 
            # the value of the second sub-packet; otherwise, the value is 0
            # These packets always have exactly two sub-packets
            self.value = int(sub_vals[0] == sub_vals[1])
        
        
    def print(self, pre=''):
        print(pre+'Version: {}'.format(self.version))
        print(pre+'Type ID: {}'.format(self.type_id))
        print(pre+'Literal Value: {}'.format(self.value))

        for p in self.sub_packs:
            p.print('\t'+pre)


def count_versions(packet):
    version_sum = packet.version 
    for p in packet.sub_packs:
        version_sum += count_versions(p)

    return version_sum


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile) 
        data = np.array([[value for value in row] for row in data])
    return data


def process_data(raw_data):
    return (bin(int(raw_data, 16))[2:]).rjust(len(raw_data)*4, '0')


def first_half(transmission):
    p = Packet()
    t = p.parse_transmission(transmission)
    solution = count_versions(p)
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(transmission):
    p = Packet()
    t = p.parse_transmission(transmission)
    solution = p.value 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    for hex_packet in data:
        print(hex_packet[0])
        bin_packet = process_data(hex_packet[0])
        second_half(bin_packet)


if __name__ == '__main__':
    main()
