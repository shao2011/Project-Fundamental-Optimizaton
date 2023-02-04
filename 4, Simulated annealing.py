import random as rd
import time, math
from ortools.sat.python import cp_model

class State:
    def __init__(self) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.value = 0
    
    """ Đề xuất chỉnh sửa Value """
    def SetValue(self):
        for i in range(m):
            sumRow = 0
            for j in range(n):
                sumRow += self.matrix[i][j]
            self.value = max(self.value,sumRow)
        self.value = self.value
    
    def RandomNeighbor(self):
        new = State()
        for i in range(m):
            for j in range(n):
                new.matrix[i][j] = self.matrix[i][j]
        
        for j in range(n):
            count12 = m**2
            
            while count12 >0:
                i1, i2 =[rd.randint(0,m-1) for t in range(2)]
                count12 -= 1
                if c[i1][j] + c[i2][j] == 2 and new.matrix[i1][j] + new.matrix[i2][j] == 1 and i1 != i2:
                    break
            if count12 == 0:
                continue
            new.matrix[i1][j] = 1 - new.matrix[i1][j]
            new.matrix[i2][j] = 1 - new.matrix[i2][j]
        
        new.SetValue()

        return new           

def initalState(number_solutions):

    model = cp_model.CpModel()
    x = [[model.NewIntVar(0,1,'x'+str(i)+str(j)) for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            model.Add(x[i][j] <= c[i][j])
    for j in range(n):
        sumCol= 0
        for i in range(m):
            sumCol += x[i][j]
        model.Add(sumCol >= k)
        model.Add(sumCol <= k)
    
    solutionList = list()
    class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
        
        nonlocal solutionList
        def __init__(self, variables, limit):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.__variables = variables
            self.__solution_count = 0
            self.__solution_limit = limit
        
        def on_solution_callback(self):
            self.__solution_count += 1
            feasibleMatrix = [[self.Value(self.__variables[i][j]) for j in range(n)] for i in range(m)]
            solutionList.append(feasibleMatrix)
              
            if self.__solution_count == self.__solution_limit:
                self.StopSearch()

    solver = cp_model.CpSolver()    
    solution_printer = VarArraySolutionPrinter(x,number_solutions)
    solver.parameters.enumerate_all_solutions = True
    solver.Solve(model, solution_printer)


    new = State()
    new.matrix = solutionList[rd.randrange(0,len(solutionList))]
    new.SetValue()

    # print("Gen xong initial")
    return new

def schedule(t):
    """ Đề xuất chỉnh sửa hàm Schedule"""
    if t <= 30:
        temperature = 100 - t
    elif t <= 70:
        a = 100 -t
        temperature = a/(a/10+1)
    else:
        temperature= (100-t)/10
    return temperature

def simulatedAnnealing():
    """Đề xuất chỉnh sửa timeLimit"""
    timeLimit = 100
    current = initalState(number_solutions= 10)
    # print(current.value)
    # time.sleep(3)
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
        # time.sleep(3)
    return current

inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1

answer = simulatedAnnealing()
AssignedPlan = [[] for j in range(n)]
for i in range(m):
    for j in range(n):
        if answer.matrix[i][j] == 1:
            AssignedPlan[j].append(i+1)
print(n)
for row in AssignedPlan:
    print(k,*row)
