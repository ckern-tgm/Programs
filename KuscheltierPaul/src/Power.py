import psutil
from hedgehog.client.sync_client import HedgehogClient

class Power(object):

    battery = psutil.sensors_battery()
    #plugged = battery.power_plugged
    percent = str(battery.percent)

    def getPower(self):
        if self.battery.percent <= 20:
            HedgehogClient.set_digital_output(8, True)
        else:
            HedgehogClient.set_digital_output(8,False)
