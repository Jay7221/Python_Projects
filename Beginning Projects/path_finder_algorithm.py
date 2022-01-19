def path(i, j, n, grid, count = 0):
    if i < 1 or j < 1 or i > n or j > n:
        print("break")
        return
    print(i, j)
    if i == n and j == n:
        flag = True
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b] == False:
                    flag = False
        if flag:
            print("count += 1")
            count += 1
    
        
    if (grid[i + 1][j] == True) and (grid[i - 1][j] == True) and (grid[i][j + 1] == False) and  (grid[i][j - 1] == False):
        return
    if (grid[i + 1][j] == False) and (grid[i - 1][j] == False) and (grid[i][j + 1] == True) and (grid[i][j - 1] == True):
        return
    if grid[i + 1][j] == False:
        grid[i + 1][j] = True
        path(i + 1, j , n, grid, count)
        grid[i + 1][j] = False

    if grid[i - 1][j] == False:
        grid[i - 1][j] = True
        path(i - 1, j , n, grid, count)
        grid[i + 1][j] = False

    if grid[i][j + 1] == False:
        grid[i][j + 1] = True
        path(i, j + 1 , n, grid, count)
        grid[i][j + 1] = False

    if grid[i][j - 1] == False:
        grid[i][j - 1] = True
        path(i, j - 1 , n, grid, count)
        grid[i][j - 1] = False

i = 1
j = 1
n = 4
count = 0
grid = list()
for a in range(n + 2):
    grid.append(list())
    for b in range(n + 2):
        grid[a].append(False)
        if a == n or b == n or a == 0 or b == 0:
            grid[a][b] = True

path(i, j, n, grid, count)
print("Count : " , count)


