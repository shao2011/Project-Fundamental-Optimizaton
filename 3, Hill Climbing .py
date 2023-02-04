import random as rd
import time
from ortools.sat.python import cp_model

class State:
    def __init__(self) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.value = 0
        
def initalState(number_solutions):

    model = cp_model.CpModel()
    x = [[model.NewIntVar(0,1,'x'+str(i)+str(j)) for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            model.Add(x[i][j] <= c[i][j])
    for j in range(n):
        sumRow= 0
        for i in range(m):
            sumRow += x[i][j]
        model.Add(sumRow >= k)
        model.Add(sumRow <= k)
    
    solutionList = list()
    class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
        """Print intermediate solutions."""
        nonlocal solutionList
        def __init__(self, variables, limit):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.__variables = variables
            self.__solution_count = 0
            self.__solution_limit = limit
        
        def on_solution_callback(self):
            self.__solution_count += 1
            feasibleMatrix =[[] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    feasibleMatrix[i].append(self.Value(self.__variables[i][j]))
            solutionList.append(feasibleMatrix)
              
            if self.__solution_count == self.__solution_limit:
                self.StopSearch()

    solver = cp_model.CpSolver()    
    solution_printer = VarArraySolutionPrinter(x,number_solutions)
    solver.parameters.enumerate_all_solutions = True
    solver.Solve(model, solution_printer)
    new = State()
    randomMatrix = rd.randrange(0,len(solutionList))

    for i in range(m):
        sumRow = 0
        for j in range(n):
            new.matrix[i][j] = solutionList[randomMatrix][i][j]
            sumRow += new.matrix[i][j]
        new.value = max(new.value,sumRow)
    new.value = n - new.value

    return new

def CalValue(state: State,list_replace):
    for j in range(n):
        i1, i2 = list_replace[j]
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

def RandomHigherSuccessor(state):
    neighbors = 0
    ''' số neighbors tỉ lệ thuận với input size'''
    while neighbors <= max(n,m):
        list_replace = []
        for j in range(n):
            count12 = 0
            while count12 < m**2:
                i1 = rd.randint(0,m-1)
                i2 = rd.randint(0,m-1)
                count12 += 1
                if c[i1][j] + c[i2][j] == 2 and state.matrix[i1][j] != state.matrix[i2][j] and i1 != i2:
                    break
            if count12 == m**2:
                i1 = None
                i2 = None
            list_replace.append([i1,i2])
            
        tempValue = CalValue(state,list_replace)
        if tempValue > state.value:
            state.value = tempValue
            return state
        
        for j in range(n):
            i1, i2 = list_replace[j]
            if i1== None: continue
            u = state.matrix[i1][j] 
            state.matrix[i1][j] = state.matrix[i2][j]
            state.matrix[i2][j] = u
        neighbors += 1
    return [None,state]

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
    neighbors = 0
    ''' số neighbors tỉ lệ thuận với input size'''
    while neighbors <= max(n,m):
        list_replace = [[j] for j in rd.sample(range(n),rd.randint(1,n))]
        
        for t in range(len(list_replace)):
            count12 = 0
            j = list_replace[t][0]
            while count12 < m**2:
                i1 = rd.randint(0,m-1)
                i2 = rd.randint(0,m-1)
                count12 += 1
                if c[i1][j] + c[i2][j] == 2 and state.matrix[i1][j] != state.matrix[i2][j] and i1 != i2:
                    break
            if count12 == m**2:
                i1 = None
                i2 = None
            list_replace[t].extend([i1,i2])
            
        tempValue = CalValueTest(state,list_replace)
        if tempValue >= state.value:
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
    current = initalState(30)
    # step = 0
    while True:
        RandomHigherNeighbor = RandomHigherSuccessor(current)
        if type(RandomHigherNeighbor) == list:
            return RandomHigherNeighbor[1]
        # step += 1
        # print("Step:",step,'|',"Value:",n-RandomHigherNeighbor.value)
    

inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1

AssignedPlan = [[] for j in range(n)]
answer = FirstChoiceHillClimbing()
for i in range(m):
    for j in range(n):
        if answer.matrix[i][j] == 1:
            AssignedPlan[j].append(i+1)
print(n)
for row in AssignedPlan:
    print(k,*row)

