from .device import *

class GardenaSmartMower(GardenaSmartDevice):
    def __init__(self, location, raw_data):
        super().__init__(location, raw_data)
        self.category = "mower"

    def start(self, duration_in_minutes=1440):
        """
        Manually start the mower, overriding the mower timer.
        The mower will work for the specified time duration - mowing and recharging.
        Once the specified duration is over, it will resume its normal schedule.
        
        :param duration_in_minutes: the duration during which the mower should mow.
        """
        self.send_command('start_override_timer', {'duration': duration_in_minutes})

    def park_until_timer(self):
        """
        Park a mower until the next timer wakes it up again.
        """
        self.send_command('park_until_next_timer')

    def park(self):
        """
        Park a mower until it is manually resumed again using either `start()` or `resume_schedule()`.
        """
        self.send_command('park_until_further_notice')
    
    def resume_schedule(self):
        """
        Resume the mower scheduler. This cancels the effects of `park()` and `start()`.
        """
        self.send_command('start_resume_schedule')

    def get_manual_operation(self):
        return self.get_value_of_property('robotic_mower', 'manual_operation')
    def get_status(self):
        return self.get_value_of_property('robotic_mower', 'status')
    def get_error(self):
        return self.get_value_of_property('robotic_mower', 'error')
    def get_battery_charging(self):
        return self.get_value_of_property('battery_power', 'charging')
    def get_last_error_code(self):
        return self.get_value_of_property('robotic_mower', 'last_error_code')
    def get_source_for_next_start(self):
        return self.get_value_of_property('robotic_mower', 'source_for_next_start')
    def get_timestamp_next_start(self):
        return self.get_value_of_property('robotic_mower', 'timestamp_next_start')
    def get_cutting_time(self):
        return self.get_value_of_property('robotic_mower_stats', 'cutting_time')
    def get_charging_cycles(self):
        return self.get_value_of_property('robotic_mower_stats', 'charging_cycles')
    def get_collisions(self):
        return self.get_value_of_property('robotic_mower_stats', 'collisions')
    def get_running_time(self):
        return self.get_value_of_property('robotic_mower_stats', 'running_time')

    def get_info(self):
        device_info = super().get_info()
        #add mower specific details to device info
        device_info['manual_operation'] = self.get_manual_operation()
        device_info['status'] = self.get_status()
        device_info['error'] = self.get_error()
        device_info['battery_charging'] = self.get_battery_charging()
        device_info['last_error_code'] = self.get_last_error_code()
        device_info['source_for_next_start'] = self.get_source_for_next_start()
        device_info['timestamp_next_start'] = self.get_timestamp_next_start()
        device_info['cutting_time'] = self.get_cutting_time()
        device_info['charging_cycles'] = self.get_charging_cycles()
        device_info['collisions'] = self.get_collisions()
        device_info['running_time'] = self.get_running_time()
        return  device_info
