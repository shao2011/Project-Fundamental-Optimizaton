import time
def Greedy1(n,m,k,l):
    
    ans = [[] for i in range(m)]

    def chonbaiBao(x):
        nonlocal n,m,k,l

        l[x].sort(key = lambda a: len(ans[a-1]))
        for i in range(k):   
            ans[l[x][i]-1].append(x+1)
            
    thu_tu = [i for i in range(n)]
    thu_tu.sort(key = lambda i: len(l[i]))

    for ele in thu_tu:
        chonbaiBao(ele)
    # kq = max([len(ans[i]) for i in range(m)])
    return ans

def input(inputPath):
    with open(inputPath, "r") as f:
        [n,m,k] = [int(i) for i in f.readline().split()]
        l = []
        for i in range(n):
            l.append([int(y) for y in f.readline().split()])
    return n,m,k,l


inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
n, m, k ,l = input(inputPath)
answer = Greedy1(n,m,k,l)


AssignedPlan = [[] for j in range(n)]
for i in range(m):
    for j in answer[i]:
        AssignedPlan[j-1].append(i+1)
print(n)
for row in AssignedPlan:
    print(k,*row)