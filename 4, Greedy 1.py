import time
def heuGen2(n,m,k,l):
    
    ans = [[] for i in range(m)]

    def chonbaiBaoGen2(x):
        nonlocal n,m,k,l

        l[x].sort(key = lambda a: len(ans[a-1]))

        for i in range(k):   
            ans[l[x][i]-1].append(x+1)
            
    thu_tu = [i for i in range(n)]
    thu_tu.sort(key = lambda i: len(l[i]))

    for ele in thu_tu:
        chonbaiBaoGen2(ele)

    kq = max([len(ans[i]) for i in range(m)])
    for row in ans:
        print(*row)

    return kq, ans

def input(inputPath):
    with open(inputPath, "r") as f:
        [n,m,k] = [int(i) for i in f.readline().split()]
        l = []
        for i in range(n):
            l.append([int(y) for y in f.readline().split()])
    return n,m,k,l

path = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
n, m, k ,l = input(path)
result, answer = heuGen2(n,m,k,l)
print("Minimum objective function:",result)
print('The plan is:')
for i in range(m):
    print('Scientist',i+1,'reviews:',*answer[i])

