from queue import PriorityQueue
import copy

global solutionType


def eucDistance(x1, y1, x2, y2): # calculates the euclidean distance between 2 coordinates
    temp1 = pow((x2  - x1), 2)
    temp2 = pow((y2 - y1), 2)
    return int((temp1 + temp2) ** 0.5)

def getCoordinates(tile): # returns the intended x and y coordinates of a tile
    if (tile == 0):
        return [2, 2]
    cnt = 1
    for i in range(0, 3):
        for j in range(0, 3):
            if (tile == cnt):
                return [i, j]
            cnt += 1
    print("tile does not exist:", tile)
    return -1 # tile does not exist



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

    # calculate the heuristic
    def h(self, curr):
        if (solutionType == "Uniform Cost"):
            return 0
        elif (solutionType == "Misplaced Tile"):
            numMisses = 0
            correctTile = 1

            # increment numMisses for each tile not in the correct spot
            for i in range(0, 3):
                for j in range(0, 3):
                    if (correctTile == 9):
                        if curr.state[2][2] != 0:
                            numMisses += 1
                    elif (curr.state[i][j] != correctTile):
                        numMisses += 1
                    correctTile += 1
            # return the number of misses as the heuristic 
            return numMisses

        else: # Euclidean Distance
            heuristic = 0
            correctTile = 1

            # heuristic is the summation of all the euc distances
            for i in range(0, 3):
                for j in range(0, 3):
                    coords = getCoordinates(curr.state[i][j])
                    heuristic += eucDistance(coords[0], coords[1], i, j)
                    correctTile += 1
            #print("huristic for state _ is ", curr.state, heuristic)
            return heuristic

    def __lt__(self, node): # sorting function for priority queue
        return (self.depth + self.h(self)) < (node.depth + self.h(node))


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
    state_i = [[1, 2, 3], [4, 8, 0], [7, 6, 5]] # default puzzle

    # handle input
    choice = input("Welcome to hcoop006 8 puzzle solver. Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")

    if (choice == '2'):
        inp = input("Enter your puzzle, use a zero to represent the blank: ")
        k = 0
        for i in range(0, 3):
            for j in range(0, 3):
                state_i[i][j] = int(inp[k])
                k += 1
    
    choice = input("Enter your choice of algorithm\nUniform Cost Search\nA* with the Misplaced Tile heuristic.\nA* with the Euclidean distance heuristic. ")
    global solutionType

    if (choice == '1'): 
        print("you chose ucs!")
        solutionType = "Uniform Cost"
    elif (choice == '2'): solutionType = "Misplaced Tile"
    else: solutionType = "Euclidean Distance"
            
    head = Node(state_i)
    
    print("\nStart State:", end = " ")
    head.printNode()

    problem = Problem()
    invalid = problem.getInvalidMoves(head)

    visited = [head.state] # initalize visited set and fronter
    q = PriorityQueue(maxsize = 90000)

    if ("up" not in invalid):
        q.put(problem.slideup(head))
    if ("down" not in invalid):
        q.put(problem.slidedown(head))
    if ("left" not in invalid):
        q.put(problem.slideleft(head))
    if ("right" not in invalid):
        q.put(problem.slideright(head))
    
    maxSize = 0
    solutionDepth = -1

    while (not q.empty()):
        if (q.full()):
            print("\nUnsolvable with a queue of size", q.qsize())
            break

        curr = q.get()
        visited.append(curr.state)

        if (problem.is_solution(curr)):
            print("\n-----success-----\nwinning sequence:\n")
            solutionDepth = curr.depth
            problem.outputSequence(curr)
            break

        # print("The best node to expand with g(n) =", curr.depth, "and h(n) =", curr.h(curr), "is...")

        invalid = problem.getInvalidMoves(curr)

        if ("up" not in invalid):
            temp = problem.slideup(curr)
            if temp.state not in visited:
                q.put(temp)
        if ("down" not in invalid):
            temp = problem.slidedown(curr)
            if temp.state not in visited:
                q.put(temp)
        if ("left" not in invalid):
            temp = problem.slideleft(curr)
            if temp.state not in visited:
                q.put(temp)
        if ("right" not in invalid):
            temp = problem.slideright(curr)
            if temp.state not in visited:
                q.put(temp)

        maxSize = max(maxSize, q.qsize())
        
    if q.empty():
        print("failure!")
    
    print("To solve this problem the search algorithm expanded a total of", len(visited), "nodes")
    print("The maximum number of nodes in the queue at any one time:", maxSize)
    if (solutionDepth != -1): print("The depth of the goal node was", solutionDepth)


if __name__=="__main__": 
    main()

# --- test cases --- #
# 103426758   
# 641752083   
# 871602543   
# 847150263   