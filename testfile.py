#This is the first line of the testfile
snake = "This game is called Snake."
print(snake)


#from pyladies list of lists and nested lists and for loops
def create_tab(size="."):
    row_list = []
    for a in range(size):
        row = []
        for b in range(size):
            row.append(a)
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