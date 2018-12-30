from hedgehog.client import connect
#from Medikamente import Medikamente
#from Termine import Termine
from SimonSays import SimonSays
#from Buecher import Buecher
from Puls import Puls
import psycopg2
from Power import Power
import pyttsx3
import platform

engine = pyttsx3.init()


# Die Main Klasse ist die, die alle Klassen zusammen bringt und deren Funktionen verwendet. Hier befinden sich alle Funktionen des Kuscheltiers.
class Main(object):


    def __init__(self):
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

    #Hier werden die Sensoren und Buttons inizialisiert
        with connect() as hedgehog:
            self.rHand = hedgehog.get_digital(1)
            self.lHand = hedgehog.get_digital(2)
            self.lFuss = hedgehog.get_digital(3)
            self.rFuss = hedgehog.get_digital(4)
            self.lOhr = hedgehog.get_digital(5)
            self.pulsSanalog = hedgehog.get_analog(5)
            self.abbr = hedgehog.get_digital(6)
            self.notfall = hedgehog.get_digital(7)

    # Hier wird die PostgreSQL Verbindung inizialisiert
        conn = psycopg2.connect("dbname=paul user=vinc password=vinc")

        # Hier werden Objekte der benötigten Klassen erstellt
        #self.m = Medikamente(conn)
        #self.t = Termine(conn,self.rFuss)
        self.s = SimonSays(conn,self.rHand,self.lHand,self.rFuss,self.lFuss, self.abbr, self.notfall)
        #self.b = Buecher(conn, self.rHand)
        self.p = Puls(self.lOhr, self.pulsSanalog)
        self.pwr = Power()

    #def thread():
        #pass
    # Die Methode ruft alle benötigten Funktionen der Klassen auf
    def callFunctions(self):
        engine.say("Wenn Sie ein Spiel spielen wollen, drücken Sie meine rechte Hand. Wenn Sie ein Höhrbuch hören wollen, drücken Sie meine linke Hand. Wenn Sie Ihre heutigen Termine hören wollen, drücken Sie meinen rechten Fuß.")
        self.pwr.getPower()
        if self.rHand == True:
            self.s.getSimonSays()
        elif self.lHand == True:
            self.b.getBuecher()
        elif self.rFuss == True:
            self.t.getTermine()
        elif self.lOhr == True:
            self.p.getPuls()
        #thread = Process(target=f, args=('bob',))
        #thread.start()
        while True:
            self.pwr.getPower()
            #self.m.getMedikamente()



# Hier wird die Methode callFunctions ausgeführt.
if __name__ == '__main__':
    m = Main()
    m.callFunctions()





