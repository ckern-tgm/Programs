from flask import Flask
from flask_restful import Resource, Api, reqparse
from Adafruit_BME280 import *



app = Flask('SimpleUserDatabase')
api = Api(app)

class server(Resource):


    def getTemperature(self):
        sensor = sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        while True:
            temperature = sensor.read_temperature()
            return temperature


    def getPressure(self):
        sensor = sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        while True:
            pressure = sensor.read_pressure()
            return pressure

    def getLight(self):
        return 25.3

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('temperature', type=str, location='args')

        temperature = parser.parse_args().temperature

        self.data = []
        self.data += [
            {
                "temperature":1.1,
                "pressure":2.2,
                "light":3.3
            }
        ]

        for data in self.data:
            data['temperature'] = self.getTemperature()
            data['pressure'] = self.getPressure()
            data['light'] = self.getLight()
            return data

api.add_resource(server,'/data')


if __name__ == '__main__':
    app.run(debug=True)


