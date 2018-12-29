import psutil
import pyttsx3
import platform

engine = pyttsx3.init()


# Startet den Vibrationsmotor, wenn der Akkustand unter 20% ist.
class Power(object):

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "german"
        engine.setProperty('rate', 140)

    engine.setProperty('voice', deutsch)

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "german"
        engine.setProperty('rate', 140)
        engine.setProperty('volume', 20)
    engine.setProperty('voice', deutsch)

    battery = psutil.sensors_battery()
    #plugged = battery.power_plugged

    # Wenn der aktuelle Akkustand geringer als oder gleich 20% ist, dann wird der Vibrationsmotor gestartet. Wenn der Akkustand höher als 20% ist,
    # wird der Vibrationsmotor wieder deaktiviert.
    def getPower(self):
        if self.battery.percent <= 20:
            engine.say("Lade mich bitte auf")
            engine.runAndWait()
        else:
            pass
if __name__ == '__main__':
    p = Power()
    p.getPower()
