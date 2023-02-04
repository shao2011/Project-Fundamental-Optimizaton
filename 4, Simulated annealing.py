import random as rd
import time, math

class State:
    def __init__(self) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.value = 0
    
    def SetValue(self):
        """ Đề xuất chỉnh sửa Value (SetValue) """
        for i in range(m):
            sumRow = 0
            for j in range(n):
                sumRow += self.matrix[i][j]
            self.value = max(self.value,sumRow)
        # self.value = self.value
    
    def RandomNeighbor(self):
        new = State()
        for i in range(m):
            for j in range(n):
                new.matrix[i][j] = self.matrix[i][j]
        
        for j in range(n):
            count12 = m**2
            
            while count12 >0:
                i1, i2 = rd.sample(l[j],2)
                count12 -= 1
                if new.matrix[i1][j] + new.matrix[i2][j] == 1:
                    break
            if count12 == 0:
                continue
            new.matrix[i1][j] = 1 - new.matrix[i1][j]
            new.matrix[i2][j] = 1 - new.matrix[i2][j]
        
        new.SetValue()
        return new           

def initalState():
    new = State()
    for j in range(n):
        lst_i = rd.sample(l[j],k)
        for i in lst_i:
            new.matrix[i][j] = 1
    new.SetValue()
    return new

def schedule(t):
    """ Đề xuất chỉnh sửa hàm Schedule"""
    if t <= 30:
        temperature = 100 - t
    elif t <= 70:
        a = 100 - t
        temperature = a/(a/10+1)
    else:
        temperature= (100-t)/10
    return temperature

def simulatedAnnealing():
    """Đề xuất chỉnh sửa timeLimit"""
    timeLimit = 100
    current = initalState()
    
    # print(current.value)
    
    for t in range(1,timeLimit):
        
        neighbor = current.RandomNeighbor()
        if neighbor.value < current.value:
            current= neighbor
            # print(current.value)
        else:
            temperature = schedule(t)
            deltaE = current.value - neighbor.value
            p = math.exp(deltaE/temperature)
            if rd.random() < p:
                current = neighbor
                # print(current.value)
        
    return current

inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    l = [[] for j in range(n)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1
            l[j].append(i-1)

t1 = time.time()
answer = simulatedAnnealing()
t2 = time.time()
print(t2-t1, answer.value)

# AssignedPlan = [[] for j in range(n)]
# for i in range(m):
#     for j in range(n):
#         if answer.matrix[i][j] == 1:
#             AssignedPlan[j].append(i+1)
# print(n)
# for row in AssignedPlan:
#     print(k,*row)
