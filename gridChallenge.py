def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Sort each row alphabetically
    for i in range(n):
        grid[i] = ''.join(sorted(grid[i]))
    
    # Check if each column is sorted alphabetically
    for j in range(m):
        column = [grid[i][j] for i in range(n)]
        if column != sorted(column):
            return 'NO'
    
    return 'YES'

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
print(gridChallenge(grid))
