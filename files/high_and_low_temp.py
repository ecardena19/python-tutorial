# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FIE0S4

file_path = 'C:/Users/Adrian Cardenas/Downloads/Climate_HourlyWeather.csv'

high = -1000
low = 1000
high_date = None

with open(file_path, 'r') as handle:
    # skip first line in file
    handle.readline()

    for line in handle:
        data = line.split(',')

        if data[6] == '':
            continue

        temp = float(data[6])

        if temp > high:
            high = temp
            high_date = str(data[0])

        if temp < low:
            low = temp
            low_date = str(data[0])

print('high', high, 'date:', high_date)
print('low', low, 'date:', low_date)

