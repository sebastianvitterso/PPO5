import camera
import irproximity_sensor
import ultrasonic
import reflectance_sensors
import zumo_button


class Sensob:
    def __init__(self, sensor):
        self.sensor = sensor
        self.sensor_value = []

    def update(self):
        self.sensor_value = []
            sensor.update()
            self.sensor_value.append(sensor.get_value())

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()
        self.sensor_value = []