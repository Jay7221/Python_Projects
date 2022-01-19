def PrintGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            print(grid[x][y],end="")
        print()
