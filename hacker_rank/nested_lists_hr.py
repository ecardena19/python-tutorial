
test_records = []

n = int(input())  # number of students in class

for i in range(n):
    names_scores = [str(input()), float(input())]  # creates format of nested list (string, float)
    test_records.append(names_scores)  # appends inputs into the nested list

test_records.sort(key=lambda x: x[1])  # sorts test scores from lowest to highest


lowest_grade = test_records[0][1]
second_lowest_grade = None
names = []

for tr in test_records:
    # tr ['name', grade]
    if tr[1] > lowest_grade and second_lowest_grade is None:
        second_lowest_grade = tr[1]

    if second_lowest_grade == tr[1]:
        names.append(tr[0])

names.sort()
for name in names:
    print(name)



