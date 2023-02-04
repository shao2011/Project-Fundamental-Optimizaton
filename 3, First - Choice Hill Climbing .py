import random as rd
import time, math
from ortools.sat.python import cp_model

class State:
    def __init__(self) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.value = 0

def initalState():
    new = State()
    for j in range(n):
        lst_i = rd.sample(l[j],k)
        for i in lst_i:
            new.matrix[i][j] = 1
    
    for i in range(m):
        sumRow = 0
        for j in range(n):
            sumRow += new.matrix[i][j]
        new.value= max(sumRow,new.value)
    new.value = n - new.value
    return new

def CalValueTest(state: State,list_replace):
    for t in range(len(list_replace)):
        j, i1, i2 = list_replace[t]
        if i1==None: continue
        u = state.matrix[i1][j] 
        state.matrix[i1][j] = state.matrix[i2][j]
        state.matrix[i2][j] = u
    score = 0
    for i in range(m):
        sumRow = 0
        for j in range(n):
            sumRow += state.matrix[i][j]
        score = max(score,sumRow)
    score = n - score
    return score

def RandomHigherSuccessorTest(state):
    """số neighbors tỉ lệ thuận với input size"""
    neighbors = 0
    
    while neighbors <= max(n,m):
        list_replace = [[j] for j in rd.sample(range(n),rd.randint(1,n))]
        
        for t in range(len(list_replace)):
            count12 = 0
            j = list_replace[t][0]
            while count12 < m**2:
                i1,i2 = rd.sample(l[j],2)
                count12 += 1
                if state.matrix[i1][j] + state.matrix[i2][j] == 1:
                    break
            if count12 == m**2:
                i1 = None
                i2 = None
            list_replace[t].extend([i1,i2])
            
        tempValue = CalValueTest(state,list_replace)
        if tempValue > state.value:
            state.value = tempValue
            return state
        
        for t in range(len(list_replace)):
            j, i1, i2 = list_replace[t]
            if i1== None: continue
            u = state.matrix[i1][j] 
            state.matrix[i1][j] = state.matrix[i2][j]
            state.matrix[i2][j] = u
        neighbors += 1
    return [None,state]

def FirstChoiceHillClimbing():
    current = initalState()
    # step = 0
    while True:
        RandomHigherNeighbor = RandomHigherSuccessorTest(current)
        if type(RandomHigherNeighbor) == list:
            return RandomHigherNeighbor[1]
        # step += 1
        # print("Step:",step,'|',"Value:",n-RandomHigherNeighbor.value)

inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    l = [[] for j in range(n)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1
            l[j].append(i-1)


answer = FirstChoiceHillClimbing()
AssignedPlan = [[] for j in range(n)]
for i in range(m):
    for j in range(n):
        if answer.matrix[i][j] == 1:
            AssignedPlan[j].append(i+1)
print(n)
for row in AssignedPlan:
    print(k,*row)

