import psutil
from hedgehog.client.sync_client import HedgehogClient

# Startet den Vibrationsmotor, wenn der Akkustand unter 20% ist.
class Power(object):

    battery = psutil.sensors_battery()
    #plugged = battery.power_plugged

    # Wenn der aktuelle Akkustand geringer als oder gleich 20% ist, dann wird der Vibrationsmotor gestartet. Wenn der Akkustand höher als 20% ist,
    # wird der Vibrationsmotor wieder deaktiviert.
    def getPower(self):
        if self.battery.percent <= 20:
            HedgehogClient.set_digital_output(8, True)
        else:
            HedgehogClient.set_digital_output(8,False)

if __name__ == '__main__':
    p = Power()
    p.getPower()
