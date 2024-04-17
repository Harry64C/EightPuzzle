from queue import PriorityQueue
import copy

# Definition for singly-linked list.
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
        return 1


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

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def slidedown(self, curr):  # swap the 0 with the element above it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]+1][position[1]]

        tempNode.state[position[0]+1][position[1]] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def slideleft(self, curr):  # swap the 0 with the element above it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]][position[1]-1]

        tempNode.state[position[0]][position[1]-1] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def slideright(self, curr):  # swap the 0 with the element above it
        tempNode = copy.deepcopy(curr)
        position = findZero(tempNode.state)
        tempVal = tempNode.state[position[0]][position[1]+1]

        tempNode.state[position[0]][position[1]+1] = 0
        tempNode.state[position[0]][position[1]] = tempVal

        tempNode.parent = curr
        tempNode.depth += 1

        return tempNode
    
    def is_solution(self, curr):
        return curr.state == self.goalState
    
    def outputSequence(self, curr):
        if (curr == None):
            return
        
        curr.printNode()
        self.outputSequence(curr.parent)


def main():

    state_i = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
    head = Node(state_i)

    print("\nOrigonal:", end = " ")
    head.printNode()

    problem = Problem()
    invalid = problem.getInvalidMoves(head)

    visited = [head.state] # initalize visited set and fronter
    q = PriorityQueue(maxsize = 400)

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
            print("\n-----success-----")
            print("winning sequence:")
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
    
    

    print("total number of nodes visited was ", len(visited))

if __name__=="__main__": 
    main()



# [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
# [[1, 0, 3], [4, 2, 6], [7, 5, 8]]