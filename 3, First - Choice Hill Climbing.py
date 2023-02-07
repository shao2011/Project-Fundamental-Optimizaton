import random as rd
import time, math, sys

class State:
    """ 
    A data structure for solving problem.\n
    A State has 02 attributes: matrix and value, 01 methods: setValue()
    """
    
    def __init__(self) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)] # A matrix with all elements = 0
        self.value = 0
    
    def setValue(self):
        """
        Calculate the Value - The max sum of rows of the State.matrix.\n
        PSEUDO CODE \n

        for each row in state's matrix do \n
            s = sum of that row \n
            state.value = max(state.value,s) \n
        """

        for i in range(m):
            sumRow = 0
            for j in range(n):
                sumRow += self.matrix[i][j]
            self.value = max(self.value, sumRow)

def initalState():
    """
    Generate a random State.\n
    This function is used for initializing randomly the first State.\n
    Firstly, create a State-object New. Then, for each column j, choose randomly K position in L[j]. For each chosen position, assign 1 to that position.\n
    Finally, use setValue() to calculate the value of New.
    """

    New = State()
    for j in range(n):
        lst_i = rd.sample(l[j],k)
        for i in lst_i:
            New.matrix[i][j] = 1
    
    New.setValue()
    
    return New

def RandomNeighbor(CurrentState: State):
    """
    Generate a new Neighbor from state.\n
    Choose random columns for changing.
    Then, for each column, random two changeable elements to change (swap).\n
    Note: two changeable elements are two element that satisfy the constraint 1 and they have different value (one = 0 and one = 1). 
    """
    
    #Create a object New like the state
    New = State() 
    for i in range(m):
        for j in range(n):
            New.matrix[i][j] = CurrentState.matrix[i][j]

    # Change Random columns, in each column, change 02 random elements
    ChangeColumns = [int(x) for x in rd.sample(range(n),rd.randint(1,n))]
    for j in ChangeColumns:
        count12 = 0
        while count12 < m**2:
            i1,i2 = rd.sample(l[j],2)
            count12 += 1
            if New.matrix[i1][j] + New.matrix[i2][j] == 1:
                break
        if count12 == m**2:
            continue
        u = New.matrix[i1][j]
        New.matrix[i1][j] = New.matrix[i2][j]
        New.matrix[i2][j] = u
    
    # Calculate the value of New
    New.setValue()
    return New

def RandomBetterOrEqualSuccessor(CurrentState):
    """Use a while loop to Find a random BETTER or EQUAL SUCCESSOR. If all successors are worse, return None"""
    
    count = 0  # to check if all the neighbors are worse than state ?. Because if all the neighbors are worse, the loop can be infinity
    while count < max(n,m):
        neighbor = RandomNeighbor(CurrentState) # get a random neighbor
        if neighbor.value <= CurrentState.value: # found a random neighbor better or equal
            return neighbor 
        count += 1

    return None  # all the neighbors are worse

def FirstChoiceHillClimbing():
    """
    Firstly, current state = a random initial state.
    Then, find a random neighbor that is better than or equals to the current state.
    If found a neighbor like that, choose that neighbor for climbing which means now current = that neighbor.
    Else, return current. Do that again and again in a while loop.\n

    Because in the loop, we choose the equal neighbor, so the algorithm can be stuck in a plateaux. To control this, we have a positive integer variable named controlPlateaux to control the plateaux, avoid the algorithm to get lost in a plateaux.
    This variable will increase by 1 whenever assign the Better or Equal neighbor to current. It's also reset to 0 if the algorithm has a Better neighbor to climb.
    Basically, this variable keeps track if the algorithm are climbing in a plateaux or not.
    """
    current = initalState() #initialize the first state
    controlPlateaux = 0 # to control algorithm when a Plateaux happens
    
    while controlPlateaux < 100:  
        TheChosenNeighbor = RandomBetterOrEqualSuccessor(current)
        if TheChosenNeighbor == None: #There's no neighbor better than or equal to the current
            return current

        if current.value != TheChosenNeighbor.value: # if TheChosenNeighbor has the better value than the current's then
            controlPlateaux = 0 # reset controlPlateaux = 0, else do nothing.

        current = TheChosenNeighbor # assign TheChosenNeighbor to the current 
        controlPlateaux += 1 # count the number of The Chosen Neighbor that has the equal value to the current's
    
    return current


n, m, k = [int(t) for t in sys.stdin.readline().split()]
c = [[0 for i in range(n)] for j in range(m)]
l = [set() for j in range(n)]
for j in range(n):
    for i in [int(t) for t in sys.stdin.readline().split()]:
        c[i-1][j] = 1
        l[j].add(i-1)
    l[j]= list(l[j])

answer = FirstChoiceHillClimbing()
AssignedPlan = [[] for j in range(n)]
for i in range(m):
    for j in range(n):
        if answer.matrix[i][j] == 1:
            AssignedPlan[j].append(i+1)
print(n)
for row in AssignedPlan:
    print(k,*row)

# inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/test4.txt"
# with open(inputPath,'r') as f:
#     n, m, k = [int(t) for t in f.readline().split()]
#     l = [set() for j in range(n)]
#     for j in range(n):
#         for i in [int(t) for t in f.readline().split()]:
#             l[j].add(i-1)
#         l[j]= list(l[j])
