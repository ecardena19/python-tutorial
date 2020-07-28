# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FIE0S4

file_path = 'C:/Users/Adrian Cardenas/Downloads/Climate_HourlyWeather.csv'

lis_temp = []

with open(file_path, 'r') as handle:
    # skip first line in file
    handle.readline()

    for line in handle:
        data = line.split(',')

        if data[6] == '':
            continue

        temp = float(data[6])
        lis_temp.append(temp)

avg_temp = sum(lis_temp) / len(lis_temp)

median_temp = 0.0

lis_temp.sort()

if len(lis_temp) % 2 == 0:
    median1 = lis_temp[len(lis_temp) // 2]
    median2 = lis_temp[len(lis_temp) // 2 - 1]
    median_temp = (median1 + median2) / 2
else:
    median_temp = lis_temp[len(lis_temp) // 2]

print('Average Temperature:', f'{avg_temp:.1f}')
print('Median Temperature:', f'{median_temp:.1f}')
