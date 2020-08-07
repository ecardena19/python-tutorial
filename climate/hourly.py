def data():
    file_path = 'C:/Users/Adrian Cardenas/Downloads/Climate_HourlyWeather.csv'
    lines = []

    with open(file_path, 'r') as handle:
        # skip first line in file
        handle.readline()

        for line in handle:
            lines.append(line)

    return lines
