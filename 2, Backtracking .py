def Backtracking_solution(n,m,k,c):
    x = [[0 for i in range(n)] for j in range(m)]
    ans = n

    def check_solution():
        nonlocal x
        for j in range(n):
            p = 0
            for i in range(m):
                p += x[i][j]
            if p < k:
                return False
        return True
    

    def Try(i,j):
        nonlocal ans # khởi tạo ans = n
        nonlocal x
        for v in [0,1]:
            if c[i][j] != 0:
                x[i][j] = v
            if i == m-1 and j == n-1:
                if check_solution():
                    temp = 0
                    for i_ in range(m):
                        q = 0
                        for j_ in range(n):
                            q += x[i_][j_]
                        temp = max(temp,q)
                    ans = min(temp,ans)
                    
            elif i == m-1:
                Try(0,j+1)
            else:
                Try(i+1,j)
            x[i][j] = 0
    
    Try(0,0)
    print(ans)

inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
# inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/data.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1

Backtracking_solution(n,m,k,c)