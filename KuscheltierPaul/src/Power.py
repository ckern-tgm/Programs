import psutil
import pyttsx3
import platform
import time

engine = pyttsx3.init()
Englisch = True

# Startet den Vibrationsmotor, wenn der Akkustand unter 20% ist.
class Power(object):

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "mb-de2"

        engine.setProperty('rate', 100)

    englisch = "english"

    if(Englisch==True):
        engine.setProperty('voice', englisch)
    else:
        engine.setProperty('voice', deutsch)

    engine.setProperty('volume', 1)


    def __init__(self, Sensorwerte):
        self.sensorwerte = Sensorwerte()

    # Wenn der aktuelle Akkustand geringer als oder gleich 20% ist, dann wird der Vibrationsmotor gestartet. Wenn der Akkustand höher als 20% ist,
    # wird der Vibrationsmotor wieder deaktiviert.
    def getPower(self):
        if self.sensorwerte.akku <= 362:
            if(Englisch==True):
                engine.say('Please load me')
            else:
                engine.say('Bitte lade mich auf')
            engine.runAndWait()
            time.sleep(5)

if __name__ == '__main__':
    p = Power()
    p.getPower()

