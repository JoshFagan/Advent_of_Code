#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

import numpy as np
import csv


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='-')
        data = np.array([[cave for cave in row] for row in data])
    return data


def create_graph(connections):
    graph = {key: set([]) for key in np.unique(connections)}
    for c in connections:
        graph[c[0]].add(c[1])
        if c[0] != 'start' and c[1] != 'end':
            graph[c[1]].add(c[0])

    return graph


def recursive_func(graph, cave, cave_path, small_caves, start_to_end, 
                   visited_twice):
    # graph: Dictionary mapping caves (strings) to set of caves they connect to
    # cave: String representing current cave
    # cave_path: List of caves (strings) visited so far
    # small_caves: Set of small caves (strings) that have been visited so far 
    # start_to_end: List of cave lists (lists of strings) that go from start to 
        # end without visiting small caves more than once
    print('====================')
    print(cave)
    print(cave_path)
    print(small_caves)
    print(visited_twice)

    # Check if this is "end"
    if cave == 'end':
        cave_path.append(cave)
        start_to_end.append(cave_path)
        return

    # Update path to current cave
    cave_path.append(cave)

    # Update list of small caves visited
    if cave.islower() and not cave == 'start':
        # Pass over this node to double tap
        small_caves.add(cave)
        for child in graph[cave] - small_caves:
            recursive_func(graph, child, cave_path[:], set(small_caves), 
                           start_to_end, 0)
        small_caves.remove(cave)
        
        # Double tap this node
        if visited_twice: 
            small_caves.add(cave)
        else:
            visited_twice = 1
        for child in graph[cave] - small_caves:
            recursive_func(graph, child, cave_path[:], set(small_caves), 
                           start_to_end, visited_twice)
    elif cave.isupper():
        # Visit all viable caves
        for child in graph[cave] - small_caves:
            recursive_func(graph, child, cave_path[:], set(small_caves), 
                           start_to_end, visited_twice)


def first_half(map): 
    graph = create_graph(map)
    solutions = []
    print(graph)
    recursive_func(graph, 'start', [], set([]), solutions, 1)
    solution = len(solutions) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(map):
    graph = create_graph(map)
    solutions = []
    recursive_func(graph, 'start', [], set([]), solutions, 0)
    print('-------------')
    for sol in solutions:
        print(sol)
    solution = len(solutions) 
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
