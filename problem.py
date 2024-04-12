
# Definition for singly-linked list.
class Node:
    state = []
    parent = None
    
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def printNode(self):
        print(self.state)


class Problem:
    def __init__(self, initialState):
        self.initialState = initialState
        self.goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def slideup(state):
        # swap the 0 with the element above it
        state[0][2] = 0
        state[1][2] = 3

    def printProblem(state):
        print(state)



def main():

    state_i = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
    problem = Problem(state_i)
    
    problem.printProblem(state_i)
    problem.slideup(state_i)
    problem.printProblem(state_i)

if __name__=="__main__": 
    main() 