# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FIE0S4


def cel_to_far(c):
    far_temp = c*(9/5) + 32
    return far_temp


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

print('high', cel_to_far(high), 'date:', high_date)
print('low', cel_to_far(low), 'date:', low_date)




