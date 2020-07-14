n = int(input())

ls = []

for _ in range(n):
    instruction = input()

    if 'insert' in instruction:
        # insert 3 11 => [insert, 3, 11]
        items = instruction.split()
        index = int(items[1])
        obj = int(items[2])
        ls.insert(index, obj)

    if 'print' in instruction:
        print(ls)




