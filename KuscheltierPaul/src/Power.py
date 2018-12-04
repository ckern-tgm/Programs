import psutil

class Power(object):

    battery = psutil.sensors_battery()
    #plugged = battery.power_plugged
    percent = str(battery.percent)


    def __init__(self, vibmotor):
        pass
        self.vibmotor = vibmotor

    def getPower(self):
        if self.battery.percent <= 20:
            self.vibmotor


