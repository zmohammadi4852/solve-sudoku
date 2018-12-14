def solve(grid,x,y,alist):
    if x == 9:

        alist.append(grid)
        print(grid)
        return alist

    v = grid[x][y]

    if v == 0:
        for i in range(1,10):

            ch = True
            if i in grid[x]:
                ch = False
                continue
            for row in range(0,9):
                if i == grid[row][y]:
                    ch = False
                    continue

            for row in range(3*(x//3),3*(x//3)+3):
                for col in range(3*(y//3),3*(y//3)+3):
                    if i == grid[row][col]:
                        ch = False
                        continue
            if ch == True:
                grid[x][y]= i
                if y < 8:
                    solve(grid,x,y+1,alist)

                else:
                    solve(grid,x+1,0,alist)
        grid[x][y] = 0
        return alist
    else:
        if y< 8:
            solve(grid,x,y+1,alist)
        else:
            solve(grid,x+1,0,alist)

        return alist


problem = [[4, 0, 3, 0, 2, 0, 6, 0, 0],
                          [9, 6, 0, 3, 0, 0, 0, 0, 0],
                          [2, 0, 1, 0, 0, 6, 0, 9, 0],
                          [0, 0, 8, 1, 0, 2, 9, 0, 0],
                          [7, 2, 0, 0, 6, 0, 0, 0, 8],
                          [0, 0, 6, 7, 0, 8, 2, 0, 0],
                          [0, 0, 2, 6, 0, 9, 5, 0, 0],
                          [8, 0, 0, 2, 0, 3, 0, 0, 9],
                          [0, 0, 5, 0, 1, 0, 3, 0, 0]]
alist = []
for a in solve(problem,0,0,alist):
    print(a)
