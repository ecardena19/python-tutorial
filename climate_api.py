from climate import hourly
from datetime import datetime
from flask import Flask
import json


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

    @classmethod
    def from_json(cls, json_str):
        """
        Given a JSON ClimateHour string, convert to ClimateHour
        instance.
        """
        json_dict = json.loads(json_str)
        return ClimateHour(**json_dict)


# convert csv data to a class, then print as JSON

# 4/1/2012 0:00	2012	4	1	0:00		4.3		2.3		87		30		28		12.9		99.88						Rain
# ClimateHour(temp, weather, rel_humidity, etc. )
# [{temp: 10.4, weather: "Rainy", rel_humidity: 23.3}, {temp: ...}]

line_count = 0
climate_hours = {}

for line in hourly.data():
    line_count = line_count + 1
    data = line.split(',')
    if data[6] == '':
        continue
    if data[8] == '':
        continue

    # "4/1/2012  12:00:00" -> datetime -> strftime('%Y-%m-%d-%h')
    date = datetime.strptime(data[0], '%Y-%m-%d %H:%M')
    climate_hour = ClimateHour(
        line_count,
        date,
        float(data[6]),
        float(data[8])
    )
    key = climate_hour.date.strftime('%Y-%m-%d-%H')
    climate_hours[key] = climate_hour

    # climate_hour_json = json.dumps(climate_hour.__dict__)
    # print(climate_hour_json)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello, {}!'.format(name)


@app.route('/hello/<name>.json')
def hello_name_json(name):
    text = 'Hello, {}!'.format(name)
    return {'text': text}


@app.route('/time.json')
def date_time_json():
    text = datetime.utcnow()
    return {'date': text}

# /climate.json?date=2012-10-01-12
# /climate.json?date=2013-10-03-12



# start the http server
app.run(debug=True)
