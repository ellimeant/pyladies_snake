map = [['.','.','.\n'],['.','.','.'],['.','.','.']]

print(map)

grid = [["." for variable in range(10)] for variable in range(10)]

# Print the grid
for row in grid:
    print(*row)


a = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
for dot in a:
    print(*dot)

b = [["c", "a", "r"], ["d", "o", "g"], ["p", "e", "t"]]
for dot in b:
    print(*dot)
    
first_element_of_second_list = b[1][0]

print(first_element_of_second_list)