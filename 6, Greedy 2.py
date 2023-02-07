# Lấy các hằng số (các input)
# n là số đề tài
# m là số giáo sư
import time
def input(inputPath):
    with open(inputPath, "r") as f:
        [n, m, k] = [int(i) for i in f.readline().split()]
        c = [[0 for i in range(n)] for j in range(m)]
        for j in range(n):
            for i in [int(g) for g in f.readline().split()]:
                c[i-1][j] = 1
    return n, m, k, c

n,m,k,c = input("input_data1")


max_paper = [0 for i in range(m)]
max_prof = [0 for j in range(n)]

for i in range(m):
    maxPaper = 0
    for j in range(n):
        if c[i][j] == 1:
            maxPaper += 1
    max_paper[i] = maxPaper

for j in range(n):
    prof_paper = 0
    for i in range(m):
        if c[i][j] == 1:
            prof_paper += 1
    max_prof[j] = prof_paper


for j in range(n):
    if max_prof[j] > k:
        res = []
        for i in range(m):
            if c[i][j] == 1:
                res.append([max_paper[i], i])
        res.sort(reverse = True)
        cut = max_prof[j] - k
        cut_lst = res[:cut]
        for l in cut_lst:
            max_paper[l[1]] -= 1
            c[l[1]][j] = 0


for review in c:
    print(*review)

print(max(max_paper))
