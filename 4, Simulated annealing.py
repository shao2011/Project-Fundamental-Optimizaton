import random as rd
import time, math, sys

class State:

    def __init__(self) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.value = 0
    
    def setValue(self):
        for i in range(m):
            sumRow = 0
            for j in range(n):
                sumRow += self.matrix[i][j]
            self.value = max(self.value,sumRow)
        
def initalState():

    New = State()
    for j in range(n):
        lst_i = rd.sample(l[j],k)
        for i in lst_i:
            New.matrix[i][j] = 1
    New.setValue()
    return New

def RandomNeighbor(state):

    New = State()
    for i in range(m):
        for j in range(n):
            New.matrix[i][j] = state.matrix[i][j]
        
    for j in range(n):
        count12 = m**2
            
        while count12 >0:
            i1, i2 = rd.sample(l[j],2)
            count12 -= 1
            if New.matrix[i1][j] + New.matrix[i2][j] == 1:
                break
        if count12 == 0:
            continue
        New.matrix[i1][j] = 1 - New.matrix[i1][j]
        New.matrix[i2][j] = 1 - New.matrix[i2][j]

    New.setValue()
    return New           

def schedule(t):
    if t <= 30:
        temperature = 100 - t
    elif t <= 70:
        a = 100 - t
        temperature = a/(a/10+1)
    else:
        temperature= (100-t)/10
    return temperature


def simulatedAnnealing():
    current = initalState()

    for t in range(1,100):

        neighbor = RandomNeighbor(current)
        if neighbor.value < current.value:
            current= neighbor

        else:
            temperature = schedule(t)
            deltaE = current.value - neighbor.value 
            p = math.exp(deltaE/temperature)
            if rd.random() < p:
                current = neighbor

    return current


n, m, k = [int(t) for t in sys.stdin.readline().split()]
c = [[0 for i in range(n)] for j in range(m)]
l = [set() for j in range(n)]
for j in range(n):
    for i in [int(t) for t in sys.stdin.readline().split()]:
        c[i-1][j] = 1
        l[j].add(i-1)
    l[j]= list(l[j])


answer = simulatedAnnealing()
AssignedPlan = [[] for j in range(n)]
for i in range(m):
    for j in range(n):
        if answer.matrix[i][j] == 1:
            AssignedPlan[j].append(i+1)
print(n)
for row in AssignedPlan:
    print(k,*row)

# inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
# with open(inputPath,'r') as f:
#     n, m, k = [int(t) for t in f.readline().split()]
#     c = [[0 for i in range(n)] for j in range(m)]
#     l = [set() for j in range(n)]
#     for j in range(n):
#         for i in [int(t) for t in f.readline().split()]:
#             c[i-1][j] = 1
#             l[j].add(i-1)
#         l[j] = list(l[j])
