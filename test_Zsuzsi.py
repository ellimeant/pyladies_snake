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

#test to get the X in (row 25-49)

b[0][1] = "x"
print(*b)

row1 = int(input("Type a number"))

b[row1][1] = "x"
print(*b)

#for the moment: this code doesn´t work, we tried to have the coordinates on the right side of "="
yourelement = "x"
coordinates_yourelement=grid[3][2]
#coordinates_yourelement=yourelement

print(coordinates_yourelement)

# problem: we get the dots as output ".", ".","." and not ........
#column = 1
#int(input("Type the column"))
#row = 2
#int(input("Type the row"))
#grid[row][column] = "x"
#gridnew = '\n'.join(grid)
#print(grid)