num_tests = int(input())
test_str = input().strip().split()

# [int('3'), int('2'), int('22')]
test_scores = list(map(int, test_str))

second_max = set(test_scores)  # removes duplicates in list
second_max.remove(max(second_max))  # removes max within set
print(max(second_max))


# print(a[a.count(a[0])])