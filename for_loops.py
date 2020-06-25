import unittest

tc = unittest.TestCase()

arr = [1, 2, 3, 100, 101]
for x in arr:
    print(x)
print(arr)

sum_value = 0
arr = [1, 28, 393, 2929]
for x in arr:
    sum_value = sum_value + x
tc.assertEqual(sum_value, 3351)

for x in range(2, 30, 3):
    print(x)
print(list(range(2, 30, 3)))

