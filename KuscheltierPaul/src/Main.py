from hedgehog.client.sync_client import HedgehogClient
from hedgehog.client import connect
from Medikamente import Medikamente
from Termine import Termine
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
        rHand = hedgehog.get_digital(1)
        lHand = hedgehog.get_digital(2)
        lFuss = hedgehog.get_digital(3)
        rFuss = hedgehog.get_digital(4)
        lOhr = hedgehog.get_digital(5)
        pulsSanalog = hedgehog.get_analog(5)
        abbr = hedgehog.get_digital(6)
        notfall = hedgehog.get_digital(7)

    # Hier wird die PostgreSQL Verbindung inizialisiert
    conn = psycopg2.connect("dbname=paul user=vinc password=vinc")

    # Hier werden Objekte der benötigten Klassen erstellt
    #m = Medikamente(conn)
    #t = Termine(conn,rFuss)
    s = SimonSays(conn,rHand,lHand,rFuss,lFuss, abbr, notfall)
    #b = Buecher(conn, rHand)
    p = Puls(lOhr, pulsSanalog)
    pwr = Power()

    #def thread():
        #pass
    # Die Methode ruft alle benötigten Funktionen der Klassen auf
    def callFunctions(self):

        engine.say("Wenn Sie Bücher hören wollen, drücken Sie meinen rechten Arm. Wenn Sie Simon Says spielen wollen, drücken Sie meinen rechten Arm. Wenn Sie die heutigen Termine hören wollen, drücken Sie meinen linken Fuß. Wenn Sie Ihren Puls messen wollen, legen Sie ihren Finger auf mein rechtes Ohr.")
        if self.rHand == True:
            self.s.getSimonSays()

        if self.lHand == True:
            self.b.getBuecher()

        if self.lFuss == True:
            #self.t.getTermineToday()
            pass
        self.p.getPuls()
        #thread = Process(target=f, args=('bob',))
        #thread.start()
        while True:
            self.pwr.getPower()
            #self.m.getMedikamente()
            #self.t.getTermine()


# Hier wird die Methode callFunctions ausgeführt.
if __name__ == '__main__':
    m = Main()
    m.callFunctions()





