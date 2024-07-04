# grid for game
grid = [["." for variable in range(10)] for variable in range(10)] #this creates a grid that is 10x10, 10 rows (=list) with 10 elements each


for row in grid:
    print(*row) # print the grid, the * puts each row (=list) on an individual line


# search for a specific element. First index is the nth-row, second is the index on the row, i.e. "column"
first_element= grid[0][0]
print(first_element, "first element")

