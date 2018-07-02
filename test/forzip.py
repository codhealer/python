list1 = [2, 3, 4]
list2 = [4, 5, 6]

for x, y in zip(list1, list2):
    print(x, y, '--', x * y)