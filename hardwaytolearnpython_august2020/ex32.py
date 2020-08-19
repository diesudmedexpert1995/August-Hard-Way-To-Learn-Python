the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear', 'apricot']
change = [1, 'dime', 2, 'nickel', 3, 'one']

for i in the_count:
    print(f"The counter {i}")


for item in fruits:
    print(f"Fruit: {item}")


for i in change:
    print(f"Change: {i}")


new_list = []
for i in range(0,6):
    new_list.append(i)
    print(new_list[i])
