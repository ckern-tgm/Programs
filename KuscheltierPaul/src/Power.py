import psutil

# Startet den Vibrationsmotor, wenn der Akkustand unter 20% ist.
class Power(object):

    battery = psutil.sensors_battery()
    #plugged = battery.power_plugged

    # Wenn der aktuelle Akkustand geringer als oder gleich 20% ist, dann wird der Vibrationsmotor gestartet. Wenn der Akkustand höher als 20% ist,
    # wird der Vibrationsmotor wieder deaktiviert.
    def getPower(self):
        if self.battery.percent <= 20:
            # Vibrationsmotor aktivieren
            pass
        else:
            # Vibrationsmotor deaktivieren
            pass
if __name__ == '__main__':
    p = Power()
    p.getPower()
