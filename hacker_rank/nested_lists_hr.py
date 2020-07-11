# num_students = int(input())

# student_names = list(map(str, input()))
# test_scores = list(map(int, input()))

# student_names = str(input())
# test_scores = float(input())

test_records = []

n = int(input())  # number of students in class

for i in range(n):
    names_scores = [str(input()), float(input())]  # creates nested list with two different data types
    test_records.append(names_scores)

low_scores = sorted(test_records[1])

print(low_scores)

