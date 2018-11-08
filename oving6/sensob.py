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
        self.sensor.update()
        self.sensor_value = self.sensor.get_value()

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
    
    def update(self):
        Sensob.update(self)

class UltrasonicSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)

    def update(self):
        # Sensob.update(self) - removed becuz threading
        self.sensor_value = self.sensor.get_value()
        print("Ultrasonic Sensor: \n", self.sensor_value)

    def refresh(self):
        self.sensor.update()


class GreenDirectionSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)
        self.direction = 0
        self.imager = imager2.Imager()

    def update(self):
       self.sensor_value = self.sensor.update()
       self.sensor_value = self.process_image()

    def process_image(self):
        # Skal finne den regionen med flest grønne pixler over et visst antall.
        wta_image = self.imager.map_color_wta(self.sensor_value)
        width = 200
        height = 200
        threshold = (height * region_width) / 2
        max_region = 0
        max_region_count = threshold
        regions = 5
        region_width = width / regions

        for region in range(0, regions):
            region_count = 0
            for col in range(0, region_width):
                for row in range(0, height):
                    if wta_image.get_pixel(row, region*region_width+col) == (0, 255, 0):
                            region_count += 1

                if region_count > max_region_count:
                    max_region = region + 1
                    max_region_count = region_count

        return max_region



