import camera
import imager2
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

class GreenDirectionSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)
        self.direction = 0
        self.imager = imager.Imager()

    def update(self):
       self.sensor_value = self.sensor.update()
       self.sensor_value = self.process_image()

    def process_image(self):
        wta_image = self.imager.map_color_wta(self.sensor_value)
        max_region = 0
        max_region_value = -1
        # 8 regioner

        for region in range(0, 8):
            region_count = 0
            for col in range(0, 16):
                for row in range(0, 96):
                    if wta_image[row][col*region] == (0, 255, 0):
                        region_count += 1

            if region_count > max_region_value:
                max_region = region + 1
                max_region_value = region_count

        return max_region


                
