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
        print("Reflectance Sensor: ", self.sensor_value)

    def is_at_end(self):
        if self.sensor_value[0] < 0.2 and self.sensor_value[5] < 0.2:
            return True


class IRProximitySensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)
    
    def update(self):
        Sensob.update(self)
        print("IR Proximity Sensor: ", self.sensor_value)


class UltrasonicSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)

    def update(self):
        # Sensob.update(self) - removed becuz threading
        self.sensor_value = self.sensor.get_value()
        print("Ultrasonic Sensor: ", self.sensor_value)

    def refresh(self):
        self.sensor.update()


class GreenDirectionSensob(Sensob):
    def __init__(self, sensor):
        Sensob.__init__(self, sensor)
        self.direction = 0
        self.sensor.img_width = 90
        self.sensor.img_height = 40
        self.imager = imager2.Imager(False, False, self.sensor.img_width, self.sensor.img_height)

    def update(self):
        print("Camera Sensor: ", self.direction)

    def refresh(self):
        self.sensor_value = self.sensor.update()
        self.direction = self.process_image()

    def process_image(self):
        # Skal finne den regionen med flest gronne pixler over et visst antall.
        wta_image = self.imager.map_color_wta(self.sensor_value, 0.34)
        width = self.sensor.img_width
        height = self.sensor.img_height
        regions = 3
        region_width = int(width / regions)
        threshold = (height * region_width) / 2
        max_region = 0
        max_region_count = threshold
        # print("Saving wta.jpeg")
        # wta_image.dump_image("WTA.jpeg")

        for region in range(0, regions):
            region_count = 0
            for col in range(0, region_width):
                for row in range(0, height):
                    pice = wta_image.get_pixel(region*region_width + col, row)
                    if pice[2] > 50:
                            region_count += 1

                if region_count > max_region_count:
                    max_region = region + 1
                    max_region_count = region_count

        return max_region



