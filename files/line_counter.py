# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FIE0S4

file_path = 'C:/Users/Adrian Cardenas/Downloads/Climate_HourlyWeather.csv'

line_count = 0
with open(file_path, 'r') as handle:
    for line in handle:
        line_count = line_count + 1

print(line_count)
