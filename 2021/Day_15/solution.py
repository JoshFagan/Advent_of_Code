#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

from queue import PriorityQueue
import numpy as np
import csv


def reconstruct_path(cameFrom, current):
    total_path = [current] # {current}
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path

# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def A_Star(start, goal, h, risk):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = PriorityQueue() #{start}
    openSet.put((0, (0,0)))

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = {} 

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {} 
    gScore[(0,0)] = 0

    # For node n, fScore[n] = gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = {(0,0) : float('inf')} # map with default value of Infinity
    fScore[(0,0)] = h((0,0))

    while not openSet.empty():
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        current = openSet.get()# the node in openSet having the lowest fScore[] value
        if current = goal:
            return reconstruct_path(cameFrom, current)

        #openSet.Remove(current)
        for each neighbor of current
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)

    # Open set is empty but goal was never reached
    return failure


def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile) 
#        data = np.array([[value for value in row] for row in data])

    print(data)
    return data


def process_data(raw_data):
    return 


def first_half(input): 
    solution = 'NOT DONE YET' 
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
    process_data(data)
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
