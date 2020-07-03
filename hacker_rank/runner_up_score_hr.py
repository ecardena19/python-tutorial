num_tests = int(input())

test_scores = list(map(int, input().strip().split()))

second_max = set(test_scores)  # removes duplicates in list
second_max.remove(max(second_max))  # removes max within set
print(max(second_max))
