#This is the first line of the testfile
snake = "This game is called Snake."
print(snake)


#from pyladies list of lists and nested lists and for loops
def create_tab(size=11):
    row_list = []
    for a in range(size):
        row = []
        for b in range(size):
            row.append(a*b)
            if a > 60:
                b = "X"
        row_list.append(row)
    return row_list

multiplication_tab = create_tab()

#print(multiplication_tab[2]) # two times three
#print(multiplication_tab[5]) # five times two
#print(multiplication_tab[8]) # eight times seven

# List the entire table
for row in multiplication_tab:
    for number in row:
        print(number, end = '')
    print()

#put in the game board to trial:
grid = [["." for variable in range(10)] for variable in range(10)] 

for row in grid:
    print(*row)

#game move to retain an x in the position given: if this position is in a list (= user input of 2 variables on the grid),
# then this position is meant to be "x" and not "." anymore. Question is how to define position == X, and how to tell the grid about this position.
# needs to take the coordinates of that postion as an argument to replace "." with "x".

#first thoughts:
x_list = [0][0] #position(s) where the x should be
if a in x_list: #a represents the coordinates - this does not seem to be valid to use
    a = "x" # the the element "." in that position on the grid should be replaced by "x"

#second thought:
changing_position = grid [0][0] #the problem is, that the coordinates are not replaced so this does not work. we need to change what we see in place of the coordinates
a = "." # this is what is shown in the coordinates in the variable "changing_position"
if changing_position == a: # doesn't work because it compares coordinates and the represented visual output
    a = "x"
    print(grid)
# we want to keep the variables but change what is displayed. somehow need to combine with the list of lists at the top