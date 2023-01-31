# Lấy các hằng số (các input)
# n là số đề tài
# m là số giáo sư
import time

inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for j in range(m)] for i in range(n)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[j][i-1] = 1

max_prof = [0 for i in range(m)]
for i in c:
    for j in range(m):
        if i[j] ==1:
            max_prof[j] += 1

for i in c:
    a = i.count(1)
    if a > k:
        res = []
        for j in range(m):
            if i[j] ==1:
                res.append([max_prof[j],j])
        res.sort(reverse= True)
        cut = a - k
        cut_lst = res[:cut]
        for l in cut_lst:
            max_prof[l[1]] -= 1
            i[l[1]] = 0

print('The minimum objective function: ',max(max_prof))

'''
10 9 4
7 6 8 2 
4 3 5 8 2 6 
6 1 2 4 3 7 
6 8 5 3 4 2 9 
5 3 2 1 7 8 4 9 6 
4 6 1 3 7 
2 9 1 6 4 
5 8 6 7 2 3 4 1 
9 4 2 3 8 1 
7 8 5 9 3 4

'''