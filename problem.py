from queue import PriorityQueue
import copy


# Node class that represents a single problem state
class Node:
    state = []
    parent = None
    depth = 0
    
    def __init__(self, state, parent=None):
        #print("node created with state", state)
        self.state = state
        self.parent = parent

    def printNode(self):
        print("")
        for i in self.state:
            for j in i:
                print(j, end = " ")
            print(end = "\n")

    def __lt__(self, Node): # sorting function for priority queue
        return self.depth < Node.depth


# returns the coordinates of the empty tile
def findZero(state):
    for i in range(0, 3):
        for j in range(0, 3):
            if (state[i][j] == 0):
                return [i, j]


# helper class that handles all the problem operations
class Problem:
    goalState = []

    def __init__(self):
        self.goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    
    # returns a list of invalid moves for the state
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

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def slidedown(self, curr):  # swap the 0 with the element below it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]+1][position[1]]

        tempNode.state[position[0]+1][position[1]] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def slideleft(self, curr):  # swap the 0 with the element left of it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]][position[1]-1]

        tempNode.state[position[0]][position[1]-1] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def slideright(self, curr):  # swap the 0 with the element right of it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]][position[1]+1]

        tempNode.state[position[0]][position[1]+1] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    # returns true if the current state is the solution, else false
    def is_solution(self, curr):
        return curr.state == self.goalState
    

    # travels back up to the root and outputs the current state each time
    def outputSequence(self, curr):
        if (curr == None):
            return

        curr.printNode()
        self.outputSequence(curr.parent)


def main():

    # handle input
    state_i = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    inp = input("Enter your puzzle, use a zero to represent the blank: ")
    k = 0
    for i in range(0, 3):
        for j in range(0, 3):
            state_i[i][j] = int(inp[k])
            k += 1
            
    head = Node(state_i)
    
    print("\nOriginal:", end = " ")
    head.printNode()

    problem = Problem()
    invalid = problem.getInvalidMoves(head)

    visited = [head.state] # initalize visited set and fronter
    q = PriorityQueue(maxsize = 8000)

    if ("up" not in invalid):
        q.put(problem.slideup(head))
    if ("down" not in invalid):
        q.put(problem.slidedown(head))
    if ("left" not in invalid):
        q.put(problem.slideleft(head))
    if ("right" not in invalid):
        q.put(problem.slideright(head))
    
    

    while (not q.empty()):
        if (q.full()):
            print("\nUnsolvable with a queue of size", q.qsize())
            break

        curr = q.get()

        if curr.state in visited:
            continue
        visited.append(curr.state)

        if (problem.is_solution(curr)):
            print("\n-----success-----\nwinning sequence:")
            print()
            problem.outputSequence(curr)
            break

        invalid = problem.getInvalidMoves(curr)

        if ("up" not in invalid):
            q.put(problem.slideup(curr))
        if ("down" not in invalid):
            q.put(problem.slidedown(curr))
        if ("left" not in invalid):
            q.put(problem.slideleft(curr))
        if ("right" not in invalid):
            q.put(problem.slideright(curr))

        
    if q.empty():
        print("failure!")
    
    print("total number of nodes visited was", len(visited))


if __name__=="__main__": 
    main()



# 123480765
# 103426758
# 720651483