#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import numpy as np
import csv


class Cave():
    def __init__(self, is_bing, is_small, name):
        self.name         = name
        self.connected_to = []
        self.num_visits   = 0
        self.is_big       = is_big
        self.is_small     = is_small


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='-')
        data = np.array([[cave for cave in row] for row in data])
    return data


def create_graph(connections):
    print(connections)
    graph = {key: set([]) for key in np.unique(connections)}
    for c in connections:
        graph[c[0]].add(c[1])
        # Add reciprocal connection unless:
        # - First cave is start (no cave should lead back to start)
        # - Second cave is end (end should not lead to any cave)
        if c[0] != 'start' and c[1] != 'end':
            graph[c[1]].add(c[0])

    return graph


def recursive_func(banned_caves, cave, cave_path, graph, num_revisits,
                   start_to_end):
    # banned_caves: Set of small caves (strings) that can no longer be visited 
    # cave: String representing current cave
    # cave_path: List of caves (strings) visited so far
    # graph: Dictionary mapping caves (strings) to set of caves they connect to
    # num_revisits: Number of possible revisits to a cave
    # start_to_end: List of cave lists (lists of strings) that go from start to 
        # end without visiting small caves more than once

    # Update path to current cave
    cave_path.append(cave)

    # Check if this is "end"
    if cave == 'end':
#        if cave_path not in start_to_end:
        start_to_end.append(cave_path)
        return
    
    # Handle big caves
    if cave.isupper() or cave == 'start':
        for child in graph[cave] - banned_caves:
            recursive_func(set(banned_caves), child, cave_path[:], graph, 
                           num_revisits, start_to_end)
        return

    # Handle small caves
    if cave.islower():
        # Case when a revisit to this cave is allowed
        if num_revisits > 0:
            for child in graph[cave] - banned_caves - set(['end']):
                recursive_func(set(banned_caves), child, cave_path[:], graph, 
                               num_revisits-1, start_to_end)
        # Case when a revisit to this cave is not allowed
        banned_caves.add(cave)
        for child in graph[cave] - banned_caves:
            recursive_func(set(banned_caves), child, cave_path[:], graph, 
                           num_revisits, start_to_end)



def first_half(map): 
    graph = create_graph(map)
    solutions = []
    print(graph)
    recursive_func(set(['start']), 'start', [], graph, 0, solutions)
    solution = len(solutions) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(map):
    graph = create_graph(map)
    solutions = []
    recursive_func(set(['start']), 'start', [], graph, 1, solutions)
    print('-------------')
    for sol in solutions:
        print(sol)
    solution = len(solutions) 
    print('\nSolution for second half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
