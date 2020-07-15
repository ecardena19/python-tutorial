n = int(input())
num1 = input().split()

tup = tuple(map(int, num1))

print(hash(tup))



