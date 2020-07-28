from climate import hourly

line_count = 0

for line in hourly.data():
    line_count = line_count + 1

print(line_count)
