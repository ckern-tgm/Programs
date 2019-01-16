import pyttsx3


# Liefert den Puls zurück
class Puls(object):
    engine = pyttsx3.init()

    #Init Methode zum Setzen der Werte, die man von den Parametern der Klasse bekommt
    def __init__(self, sensorwerte):
       self.sensorwerte = sensorwerte


    # Die Methode überprüft, ob der Pulssensor verwendet wird. Wenn der Pulssensor verwendet wird, werden die Werte vom Pulssensor zurück gegeben.
    # Der Thread für das Unterbrechen der Methode muss noch implementiert werden.
    # Wird ausgeführt, wenn Sensor berührt wird und gestoppt, wenn sensor nicht mehr berührt wird
    def getPuls(self):
        while self.sensorwerte.lOhr == True:
            self.engine.say(self.sensorwerte.pulsAnalog)
            self.engine.runAndWait()
        print (self.sensorwerte.pulsAnalog)


