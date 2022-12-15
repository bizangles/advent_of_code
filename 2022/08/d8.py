with open('input') as fh:
    grid = [line.strip() for line in fh]
    

visible = set()
rows = len(grid)
cols = len(grid[0])


for row in range(rows):
    rowmax = -1
    for col in range(cols):
        n = int(grid[row][col])
        if n > rowmax:
            rowmax = n
            visible.add((row, col))

    rowmax = -1
    for col in reversed(range(cols)):
        n = int(grid[row][col])
        if n > rowmax:
            rowmax = n
            visible.add((row, col))

for col in range(cols):
    colmax = -1
    for row in range(rows):
        n = int(grid[row][col])
        if n > colmax:
            colmax = n
            visible.add((row, col))

    colmax = -1
    for row in reversed(range(rows)):
        n = int(grid[row][col])
        if n > colmax:
            colmax = n
            visible.add((row, col))

print(len(visible))
