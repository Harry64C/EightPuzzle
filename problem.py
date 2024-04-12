from collections import deque
import copy

# Definition for singly-linked list.
class Node:
    state = []
    parent = None
    
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def printNode(self):
        for i in self.state:
            for j in i:
                print(j, end = " ")
            print(end = "\n")


def findZero(state):
    for i in range(0, 3):
        for j in range(0, 3):
            if (state[i][j] == 0):
                return [i, j]

class Problem:
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self):
        self.goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


                
    def getInvalidMoves(self, curr):
        position = findZero(curr.state)
        invalid = []

        if (position[0] <= 0):
            invalid.append("up")
        elif (position[0] >= 2):
            invalid.append("down")

        if (position[1] <= 0):
            invalid.append("left")
        elif (position[1] >= 2):
            invalid.append("right")

        return invalid


    def slideup(self, curr):  # swap the 0 with the element above it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]-1][position[1]]

        tempNode.state[position[0]-1][position[1]] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        return tempNode


def main():

    state_i = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
    head = Node(state_i)

    problem = Problem()
    invalid = problem.getInvalidMoves(head)

    visited = [] # initalize visited set and fronter
    q = deque()
    if ("up" not in invalid):
        q.append(problem.slideup(head))
    
    node = q.popleft()
    node.printNode()

if __name__=="__main__": 
    main() 