n = int(input().strip())

result1 = 'Weird'
result2 = 'Not Weird'

if n % 2 == 0:
    if 2 <= n <= 5:
        print(result2)
    if 6 <= n <= 20:
        print(result1)
    if n > 20:
        print(result2)
else:
    print(result1)
