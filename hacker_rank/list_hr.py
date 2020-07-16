n = int(input())

ls = []

for _ in range(n):
    instruction = input()

    if 'insert' in instruction:
        # 'insert 3 11' => ['insert', '3', '11']
        items = instruction.split()
        index = int(items[1])
        obj = int(items[2])
        ls.insert(index, obj)

    if 'print' in instruction:
        print(ls)

    if 'remove' in instruction:
        items2 = instruction.split()
        index2 = int(items2[1])
        ls.remove(index2)

    if 'append' in instruction:
        items3 = instruction.split()
        index3 = int(items3[1])
        ls.append(index3)

    if 'sort' in instruction:
        ls.sort()

    if 'pop' in instruction:
        ls.pop()

    if 'reverse' in instruction:
        ls.reverse()
