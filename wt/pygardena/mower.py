from .device import *

class GardenaSmartMower(GardenaSmartDevice):
    
    __json_mappings__ = {
       'manual_operation': 'robotic_mower.manual_operation',
       'status': 'robotic_mower.status',
       'error': 'robotic_mower.error',
       'battery_charging': 'battery_power.charging',
       'last_error_code': 'robotic_mower.last_error_code',
       'source_for_next_start': 'robotic_mower.source_for_next_start',
       'timestamp_next_start': 'robotic_mower.timestamp_next_start',
       'cutting_time': 'robotic_mower_stats.cutting_time',
       'charging_cycles': 'robotic_mower_stats.charging_cycles',
       'collisions': 'robotic_mower_stats.collisions',
       'running_time': 'robotic_mower_stats.running_time',
    }
    
    def start(self, duration=1440):
        self.send_command('start_override_timer', {'duration': duration})

    def park_until_timer(self):
        self.send_command('park_until_next_timer')

    def park(self):
        self.send_command('park_until_further_notice')

    def get_manual_operation(self):
        return self.manual_operation
    def get_status(self):
        return self.status
    def get_error(self):
        return self.error
    def get_battery_charging(self):
        return self.battery_charging
    def get_last_error_code(self):
        return self.last_error_code
    def get_source_for_next_start(self):
        return self.source_for_next_start
    def get_timestamp_next_start(self):
        return self.timestamp_next_start
    def get_cutting_time(self):
        return self.cutting_time
    def get_charging_cycles(self):
        return self.charging_cycles
    def get_collisions(self):
        return self.collisions
    def get_running_time(self):
        return self.running_time

