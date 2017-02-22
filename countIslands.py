# 1 1 1 1 0
# 1 1 0 1 0
# 1 1 0 0 0
# 0 0 0 0 0 

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0

    # leet code input was in a string, use this to convert string to ints
    newGrid = []
    for i in xrange(len(grid)):
        newGrid.append([])
        for j in xrange(len(grid[i])):
            newGrid[i].append(int(grid[i][j]))
            
    for i in xrange(len(grid)):
        for j in xrange(len(grid[i])):
            if newGrid[i][j] == 1:
                count += 1
                flip(newGrid, i, j)
    
    return count

def flip(grid, i, j):
    if i < 0 or i > len(grid)-1:
        return
    if j < 0 or j > len(grid[i])-1:
        return
    if grid[i][j] == 0 or grid[i][j] == 2:
        return

    if grid[i][j] == 1:
        grid[i][j] = 2

    flip(grid, i-1, j)
    flip(grid, i+1, j)
    flip(grid, i, j+1)
    flip(grid, i, j-1)

# grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
grid = ["11110","11010","11000","00000"]
print numIslands(grid)