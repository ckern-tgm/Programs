import pyttsx3
from threading import Thread
from Sensorwerte import Sensorwerte
import platform

Englisch = True

# Liefert den Puls zurück
class Puls(object):
    engine = pyttsx3.init()

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "mb-de2"
        engine.setProperty('rate', 100)

    englisch = "english"

    if (Englisch == True):
        engine.setProperty('voice', englisch)
    else:
        engine.setProperty('voice', deutsch)

    #Init Methode zum Setzen der Werte, die man von den Parametern der Klasse bekommt
    def __init__(self,sensorwerte):
       self.sensorwerte = sensorwerte

    # Die Methode überprüft, ob der Pulssensor verwendet wird. Wenn der Pulssensor verwendet wird, werden die Werte vom Pulssensor zurück gegeben.
    # Der Thread für das Unterbrechen der Methode muss noch implementiert werden.
    # Wird ausgeführt, wenn Sensor berührt wird und gestoppt, wenn sensor nicht mehr berührt wird
    def getPuls(self):
        while self.sensorwerte.abbr == True:
            #Thread(target=self.abbrechen()).start()
            if (Englisch == True):
                self.engine.say("Heart rate measuring has started")
            else:
                self.engine.say("Pulsmessen wurde gestartet")
            self.engine.runAndWait()
            self.engine.say(self.sensorwerte.pulsAnalog/50)
            self.engine.runAndWait()
        if (Englisch == True):
            self.engine.say("Heart rate measuring has stopped")
        else:
            self.engine.say("Pulsmessen wurde beendet")
        self.engine.runAndWait()

    def abbrechen(self):
        if self.sensorwerte.abbr == False:
            if (Englisch == True):
                self.engine.say("Heart measuring has ended")
            else:
                self.engine.say("Pulsmessen wurde beendet")
            self.engine.runAndWait()

if __name__ == '__main__':
    s = Sensorwerte()
    p = Puls(s)
    p.getPuls()
