x = int(input())
y = int(input())
z = int(input())
n = int(input())

# coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]

coordinates = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            # i=0 j=0 k=0
            # i=0 j=0 k=1
            # ...
            # i=0 j=1 k=0
            if (i + j + k) != n:
                coordinates.append([i, j, k])

print(coordinates)

