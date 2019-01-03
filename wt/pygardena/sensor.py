from .device import *

class GardenaSmartSensor(GardenaSmartDevice, GardenaDisposableBatteryMixin, GardenaAmbientTemperatureMixin):
    
    __json_mappings__ = {
        'soil_temperature': 'soil_temperature_sensor.temperature',
        'soil_humidity': 'soil_humidity_sensor.humidity',
        'light': 'light_sensor.light',
    }

    def get_soil_temperature(self):
        return self.soil_temperature
    def get_soil_humidity(self):
        return self.soil_humidity
    def get_light(self):
        return self.light
