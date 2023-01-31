import random as rd
import math

class State:
    def __init__(self,n,m) -> None:
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        self.value = None
        self.maxSumRow = 0
        
def initalState(n,m):
    global c
    new = State(n,m)
    for i in range(m):
        for j in range(n):
            if c[i][j] ==1:
                new.matrix[i][j] = rd.randint(0,1)
    new.value,new.maxSumRow = CalValue(new,False,None,None)
    
    return new

def CalValue(state: State,neighbor: bool, repl_i, repl_j): 
    global c, k, n, m
    # Chỉ return ra cái số value tính được, chứ không làm thay đổi self.value
    if state == None:
        return -math.inf

    
    if not neighbor:
        kq = 0
        #constraint 2
        for j in range(n):
            p = 0
            for i in range(m):
                p+= state.matrix[i][j]
            if p >= k:
                kq += 1000
            else:
                kq -= 1000
        # Phần minimize
        for i in range(m):
            p = 0
            t = 0
            for j in range(n):
                p += state.matrix[i][j]
            t = max(p,t)
        kq += (n-t)*10
        return kq,t
    
    else:
        kq = state.value

        # Lấy tổng row repl_i và column repl_j
        p = 0
        for i in range(m):
            p += state.matrix[i][repl_j]
        q = 0
        for j in range(n):
            q += state.matrix[repl_i][j]
        
        # Gỡ điểm ra
        if p < k:
            kq += 1000
        else:
            kq -= 1000
        
        # Điểm mới
        if state.matrix[repl_i][repl_j] == 0:
            p += 1
            q += 1
        else:
            p -= 1
            q -= 1
        
        # Lắp điểm mới
        if p >= k:
            kq += 1000
        else:
            kq -= 1000
        
        if q > state.maxSumRow:
            kq -= (n-state.maxSumRow)*10
            kq += (n - q)*10
               
        return kq,q

def HighestSuccessor(state: State):
    global n,m,c
    
    best_score = -math.inf
    bestMaxSumRow = 0
    i_ans = None
    j_ans = None
    for i in range(m):
        for j in range(n):
            if c[i][j] == 1:

                temp_score,temp_MaxSumRow = CalValue(state,True,i,j)       
                if temp_score > best_score:
                    i_ans= i
                    j_ans = j
                    best_score = temp_score
                    bestMaxSumRow = temp_MaxSumRow

    state.matrix[i_ans][j_ans] = 1 - state.matrix[i_ans][j_ans]
    state.value= best_score
    state.maxSumRow = bestMaxSumRow
    return state

def HillClimbing():
    global n,m,c,k
    current = initalState(n,m) 

    while True:
        neighbor = HighestSuccessor(current)
        if neighbor.value <= current.value:
            return current
        current = neighbor



inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1
    
answer = HillClimbing()

print("Minimum objective function",answer.maxSumRow)
print('The plan is:')
for i in range(0,m):
    print("Scientist",i+1,'reviews:',*answer.matrix[i])


