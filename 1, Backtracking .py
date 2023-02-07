import sys

def Backtracking_solution(n,m,k,c):
    x = [[0 for i in range(n)] for j in range(m)]
    ans = n
    AssignedPlan = None
    def UpdateSolution():
        plan = [[] for j in range(n)]
        for i_ in range(m):
            for j_ in range(n):
                if x[i_][j_] == 1:
                    plan[j_].append(i_+1)
        return plan
    
    def check(j):
        nonlocal x
        p = 0
        for i in range(m):
            p += x[i][j]
        if p != k:
            return False
        return True
    

    def Try(i,j):
        nonlocal ans, x, AssignedPlan

        for v in set([0,c[i][j]]):
            x[i][j] = v
            if i == m-1 and j == n-1:
                if check(j):
                    temp = 0
                    for i_ in range(m):
                        q = 0
                        for j_ in range(n):
                            q += x[i_][j_]
                        temp = max(temp,q)
                    if temp < ans:
                        ans = temp
                        AssignedPlan = UpdateSolution()  

            elif i == m-1:
                if check(j):
                    Try(0,j+1)
            else:
                Try(i+1,j)
            x[i][j] = 0
    
    Try(0,0)
    print(n)
    for paper in AssignedPlan:
        print(k,*paper)

n, m, k = [int(t) for t in sys.stdin.readline().split()]
c = [[0 for i in range(n)] for j in range(m)]
for j in range(n):
    for i in [int(t) for t in sys.stdin.readline().split()]:
        c[i-1][j] = 1

Backtracking_solution(n,m,k,c)


# inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
# with open(inputPath,'r') as f:
#     n, m, k = [int(t) for t in f.readline().split()]
#     c = [[0 for i in range(n)] for j in range(m)]
#     for j in range(n):
#         for i in [int(t) for t in f.readline().split()]:
#             c[i-1][j] = 1
