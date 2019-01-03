from .account import *

class GardenaSmartDevice:
    
    # Mappings from raw_data to object attributes
    # Syntax: attribute name to path (used by get_value)
    __json_mappings__ = {
        'id': 'id',
        'name': 'name',
        'category': 'category',
        'battery_level': 'battery_power.level',
        'radio_quality': 'radio_link.quality',
        'radio_connection_status': 'radio_link.connection_status',
        'radio_state': 'radio_link.state',
    }
    
    def __init__(self, location, raw_data):
        self.location = location
        self.raw_data = raw_data
        self.update_json_mappings()
    
    def get_value(self, path):
        path_elements = path.split('.')
        if len(path_elements) == 1:
            return self.raw_data[path_elements[0]]
        if len(path_elements) == 2:
            ability_type, property_name = path_elements
            for ability in self.raw_data['abilities']:
                if ability['type'] != ability_type:
                    continue
                for property in ability['properties']:
                    if property['name'] == property_name:
                        return property['value']
        return None

    def update(self):
        self.raw_data = self.location.get_raw_device_data(self.id)
        self.update_json_mappings()
    
    def get_json_mappings(self):
        """
        Returns a dictionary of mappings between attributes and json paths for the class.
        By default, this method checks the class and all superclasses
        for the `__json_mappings__` field; the result is then combined
        into one dictionary.
        
        If there are collisions between the property mappings, then they
        are resolved in the method resolution order: later definitions
        have precendence.
        """
        property_mappings = {}
        for cls in reversed(self.__class__.__mro__):
            mapping = getattr(cls, '__json_mappings__', None)
            if mapping:
                property_mappings.update(mapping)
        return property_mappings
    
    def update_json_mappings(self):
        info = {}
        for target, path in self.get_json_mappings().items():
            value = self.get_value(path)
            setattr(self, target, value)
            info[target] = value
        self.info = info

    def get_category(self):
        return self.category
    def get_battery_level(self):
        return self.battery_level
    def get_radio_quality(self):
        return self.radio_quality
    def get_radio_connection_status(self):
        return self.radio_connection_status
    def get_radio_state(self):
        return self.radio_state
    def get_info(self):
        return self.info

    def send_command(self, name, parameters=None):
        data = {'name': name}
        if parameters is not None:
            data['parameters'] = parameters
        data = json.dumps(data)

        url = 'https://smart.gardena.com/sg-1/devices/' + self.id + '/abilities/' + self.category + '/command?locationId=' + self.location.id
        headers = self.location.gardena_hub.create_header(Token=self.location.gardena_hub.AuthToken)
        response = self.location.gardena_hub.s.post(url, headers=headers, data=data)
        # @todo, maybe check response and do some error handing?

class GardenaAmbientTemperatureMixin:
    
    __json_mappings__ = {
        'ambient_temperature': 'ambient_temperature_sensor.temperature',
        'ambient_frost_warning': 'ambient_temperature_sensor.frost_warning',
    }
    
    ambient_temperature = None
    ambient_frost_warning = None
    
    def get_ambient_temperature(self):
        return self.ambient_temperature
    def get_ambient_frost_warning(self):
        return self.ambient_frost_warning
    
class GardenaDisposableBatteryMixin:
    
    __json_mappings__ = {
        'battery_status': 'battery_power.disposable_battery_status',
    }
    
    battery_status = None
    
    def get_battery_status(self):
        return self.get_value_of_property('battery_power', 'disposable_battery_status')
    
