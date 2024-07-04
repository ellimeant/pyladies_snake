    Ich
11:17
https://github.com/ellimeant/pyladies_snake
Zsuzsanna Narducci
11:19
ZsuzsanNar
Ich
11:43
"--------"
Zsuzsanna Narducci
11:53
\n
('Our old chiming clock\n')
Ich
11:56
https://stackoverflow.com/questions/38872341/print-list-of-lists-in-separate-lines
Zsuzsanna Narducci
11:57
# Create a 10x10 grid filled with zeros
grid = [[0 for _ in range(10)] for _ in range(10)]

# Print the grid
for row in grid:
    print(row)
Ich
12:39
["foo", "bar", "baz"].index("bar")
1
Ich
12:41
To get all indexes:

indexes = [i for i, x in enumerate(xs) if x == 'foo']
Ich
12:46
.index("baz")
[-1]
[2]
Zsuzsanna Narducci
12:47
https://pyladies.at/2024/pyladies-en-vienna-2024-spring/beginners-en/str/
Ich
12:48
https://pyladies.at/2024/pyladies-en-vienna-2024-spring/beginners-en/list/
Ich
12:49
first_element_of_second_list = list_of_lists[1][0]


Ich
14:04
first_element_of_second_list = list_of_lists[1][0]
Ich
14:48
for row in multiplication_tab:
    for number in row:
        print(number, end = '')
    print()
Ich
14:51
end = " "
Ich
14:55
print(grid, sep='\n')
Ich
14:57
strValue = '\n'.join(listOfStrs)
print(strValue)
gridnew = '\n'.join(grid)
print(gridnew)
Ich
15:03
gridnew = '\n'.join(map(str, a))
https://thispointer.com/print-list-elements-on-separate-lines-in-python/