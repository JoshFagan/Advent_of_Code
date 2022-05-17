#!/Users/josh/.local/share/virtualenvs/Advent_of_Code-07aOslbA/bin/python3

from queue import PriorityQueue
import numpy as np
import csv
import sys
np.set_printoptions(threshold=np.inf, linewidth=200)


class AStar():
    def __init__(self, d, start, goal):
        self.goal = goal
        self.d = d
        self.total_risk = 0

        # The set of discovered nodes that may need to be (re-)expanded.
        # Initially, only the start node is known.
        # This is usually implemented as a min-heap or priority queue rather 
        # than a hash-set.
        openSet = PriorityQueue() #{start}
        openSet.put((0, start))

        # For node n, cameFrom[n] is the node immediately preceding it on the 
        # cheapest path from start to n currently known.
        self.cameFrom = {} 

        # For node n, gScore[n] is the cost of the cheapest path from start to 
        # n currently known.
        gScore = {} 
        gScore[start] = 0
    
        # For node n, fScore[n] = gScore[n] + h(n). 
        # fScore[n] represents our current best guess as to how short a path 
        # from start to finish can be if it goes through n.
        fScore = {start : float('inf')} # map with default value of Infinity
        fScore[start] = self.h(start) 


        # This operation can occur in O(Log(N)) time if openSet is a min-heap 
        # or a priority queue
        while not openSet.empty():
            # the node in openSet having the lowest fScore[] value
            (score, current) = openSet.get() 
            if current == goal:
                self.reconstruct_path(current)
                return
    
            for neighbor in self.get_neighbors(current):
                tentative_gScore = gScore[current] + d[neighbor]
                if tentative_gScore < gScore.get(neighbor, float('inf')):
                    # This path to neighbor is better than any previous one. 
                    self.cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + self.h(neighbor)
                    if not any(neighbor == item[1] for item in openSet.queue):
                        openSet.put((gScore[neighbor], neighbor))
    
        
    def reconstruct_path(self, current):
        self.total_path = [current]
        while current in self.cameFrom.keys():
            self.total_risk += self.d[current]
            current = self.cameFrom[current]
            self.total_path.append(current)

        self.total_path.reverse()

    
    def h(self, cell):
        return abs(self.goal[0]-cell[0]) + abs(self.goal[1]-cell[1])
    
    
    def get_neighbors(self, cell):
        neighbors = []
        offsets = [(-1,0), (1,0), (0,-1), (0,1)]
        for o in offsets: 
            neighbor = (cell[0] + o[0], cell[1] + o[1]) 
            if 0 <= neighbor[0] and 0 <= neighbor[1] and neighbor[0] < self.d.shape[0] and neighbor[1] < self.d.shape[1]:
                neighbors.append(neighbor)
    
        return neighbors



def load_data():
    # Read contents of file
    with open('data.txt', 'r') as csvfile:
        data = csv.reader(csvfile) 
        data = np.array([[int(char) for char in row[0]] for row in data])

    return data

def expand_map(old_map):
    old_map -= 1
    (num_r, num_c) = old_map.shape
    new_map = np.zeros((num_r*5, num_c*5), dtype=np.int8)
    for i in range(5):
        for j in range(5):
            new_map[num_r*i:num_r*(i+1), num_c*j:num_c*(j+1)] = (old_map+i+j)%9 

    old_map += 1
    new_map += 1

    return new_map

def first_half(risks): 
    a_star = AStar(risks, (0,0), (risks.shape[0]-1, risks.shape[1]-1))
    print(a_star.total_path)
    solution = a_star.total_risk
    
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return 
        

def second_half(risks):
    risks = expand_map(risks)
    a_star = AStar(risks, (0,0), (risks.shape[0]-1, risks.shape[1]-1))
    solution = a_star.total_risk
    print('\nSolution for first half!')
    print('SOLUTION DESCRIPTION: {}\n'.format(solution))
    return


def main():
    data = load_data() 
    first_half(data)
    second_half(data)


if __name__ == '__main__':
    main()
