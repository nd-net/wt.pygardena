from .device import *

class GardenaSmartWateringComputer(GardenaSmartDevice, GardenaDisposableBatteryMixin, GardenaAmbientTemperatureMixin):
    
    __json_mappings__ = {
        'valve_open': 'watering_outlet.valve_open',
        'manual_override': 'watering_outlet.manual_override',
        'button_manual_override_time': 'watering_outlet.button_manual_override_time',
        'last_manual_override_time': 'watering_outlet.last_manual_override_time',
        'scheduled_watering_next_start': 'scheduling.scheduled_watering_next_start',
        'scheduled_watering_end': 'scheduling.scheduled_watering_end',
        'adaptive_scheduling_last_decision': 'scheduling.adaptive_scheduling_last_decision',
    }

    def get_valve_open(self):
        return self.valve_open
    def get_manual_override(self):
        return self.manual_override
    def get_button_manual_override_time(self):
        return self.button_manual_override_time
    def get_last_manual_override_time(self):
        return self.last_manual_override_time
    def get_scheduled_watering_next_start(self):
        return self.scheduled_watering_next_start
    def get_scheduled_watering_end(self):
        return self.scheduled_watering_end
    def get_adaptive_scheduling_last_decision(self):
        return self.adaptive_scheduling_last_decision

    def start(self, duration=30):
        self.send_command('manual_override', {'duration': duration})
        self.valve_open = True

    def stop(self):
        self.send_command('cancel_override')
        self.valve_open = False

