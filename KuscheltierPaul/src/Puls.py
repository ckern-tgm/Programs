import pyttsx3
from threading import Thread
from Sensorwerte import Sensorwerte

# Liefert den Puls zurück
class Puls(object):
    engine = pyttsx3.init()

    #Init Methode zum Setzen der Werte, die man von den Parametern der Klasse bekommt
    def __init__(self,sensorwerte):
       self.sensorwerte = sensorwerte

    # Die Methode überprüft, ob der Pulssensor verwendet wird. Wenn der Pulssensor verwendet wird, werden die Werte vom Pulssensor zurück gegeben.
    # Der Thread für das Unterbrechen der Methode muss noch implementiert werden.
    # Wird ausgeführt, wenn Sensor berührt wird und gestoppt, wenn sensor nicht mehr berührt wird
    def getPuls(self):
        while self.sensorwerte.abbr == True:
            #Thread(target=self.abbrechen()).start()
            self.engine.say(self.sensorwerte.pulsAnalog/50)
            self.engine.runAndWait()
        self.engine.say("Pulsmessen wurde beendet")
        self.engine.runAndWait()

    def abbrechen(self):
        if self.sensorwerte.abbr == False:
            self.engine.say("Pulsmessen wurde beendet")
            self.engine.runAndWait()

if __name__ == '__main__':
    s = Sensorwerte()
    p = Puls(s)
    p.getPuls()
