def CP_solution_with_ortools(n,m,k,c):
    # Tạo model
    from ortools.sat.python import cp_model
    model = cp_model.CpModel()

    # Tạo các biến x_ij và tạo biến t (minimize thằng t)
    t = model.NewIntVar(0,n,'t')
    x = [[None for i in range(n)] for j in range(m)] 
    for i in range(m):
        for j in range(n):
            x[i][j] = model.NewIntVar(0,1,'x'+str(i)+str(j))

    # tạo các constraint c1
    for i in range(m):
        for j in range(n):
            model.Add(x[i][j] <= c[i][j])
    # tạo các constraint c2
    for j in range(n):
        p = 0
        for i in range(m):
            p += x[i][j]
        model.Add(p >= k)
    # tạo các constraint c3
    for i in range(m):
        p = 0
        for j in range(n):
            p += x[i][j]
        model.Add(t - p >= 0)

    # nhập hàm objective func
    model.Minimize(t)

    # Giải bài toán
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # In đáp án
    if status == cp_model.OPTIMAL:
        print(f'Minimum of objective function: {solver.ObjectiveValue()}\n')
        print("The plan is:")
        for i in range(m):
            for j in range(n):
                x[i][j] = solver.Value(x[i][j])
        for i in range(m):
            print('Scientist',i+1,'reviews:',*x[i])
    else:
        print('No solution found.')

# Replace the input file path 
inputPath = "C:/Users/ADMIN/OneDrive/Desktop/Tối ưu hoá/3, Project/3, Solution/input.txt"
with open(inputPath,'r') as f:
    n, m, k = [int(t) for t in f.readline().split()]
    c = [[0 for i in range(n)] for j in range(m)]
    for j in range(n):
        for i in [int(t) for t in f.readline().split()]:
            c[i-1][j] = 1

CP_solution_with_ortools(n,m,k,c)
