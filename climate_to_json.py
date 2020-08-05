from climate import hourly


class ClimateHour(object):
    line_no = 0
    date = None
    temp = None
    dew_point = None

    # constructor
    def __init__(self, line_no, date, temp, dew_point):
        self.line_no = line_no
        self.temp = temp
        self.date = date
        self.dew_point = dew_point

    # override default str implementation
    def __str__(self):
        return "Line#: {} Date: {} Temp: {} Dew Point: {}".format(
            self.line_no,
            self.date,
            self.temp,
            self.dew_point
        )


# convert csv data to a class, then print as JSON

# 4/1/2012 0:00	2012	4	1	0:00		4.3		2.3		87		30		28		12.9		99.88						Rain
# ClimateHour(temp, weather, rel_humidity, etc. )
# [{temp: 10.4, weather: "Rainy", rel_humidity: 23.3}, {temp: ...}]

line_count = 0

for line in hourly.data():
    line_count = line_count + 1
    data = line.split(',')
    if data[6] == '':
        continue
    if data[8] == '':
        continue

    climate_hour = ClimateHour(
        line_count,
        str(data[0]),
        float(data[6]),
        float(data[8])
    )

    print(climate_hour)
