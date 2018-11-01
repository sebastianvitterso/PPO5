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
        self.sensor.update()
        self.sensor_value.append(self.sensor.get_value())

    def reset(self):
        self.sensor.reset()
        self.sensor_value = []


class ReflectanceSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)

    def update(self):
        Sensob.update(self)
        print("Reflectance Sensor: \n", self.sensor_value)


class IRProximitySensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)


class UltrasonicSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)







