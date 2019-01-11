##from hedgehog.client.sync_client import HedgehogClient
from hedgehog.client import connect
from Sensorwerte import Sensorwerte
from Medikamente import Medikamente
#from Termine import Termine
#from Notfallsms import Notfallsms
from hedgehog.client import connect
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
    
    
    sensorwerte = Sensorwerte()

    # Hier wird die PostgreSQL Verbindung inizialisiert
    conn = psycopg2.connect("dbname=paul user=vinc password=vinc")

    # Hier werden Objekte der benötigten Klassen erstellt
    m = Medikamente(conn)
    #t = Termine(conn,sensorwerte)
    s = SimonSays(conn,sensorwerte)
    #b = Buecher(conn, sensorwerte)
    p = Puls(sensorwerte)
    
    #pwr = Power()
    #nsms = Notfallsms()

    # Die Methode ruft alle benötigten Funktionen der Klassen auf
    def callFunctions(self):

        engine.say("Wenn Sie Bücher hören wollen, drücken Sie meinen rechten Arm. Wenn Sie Simon Says spielen wollen, drücken Sie meine linken Arm. Wenn Sie die heutigen Termine hören wollen, drücken Sie meinen linken Fuß. Wenn Sie Ihren Puls messen wollen, legen Sie ihren Finger auf mein rechtes Ohr.")
        engine.runAndWait()
        while True:
            if self.sensorwerte.rHand == False:
                self.s.getSimonSays()

            if self.sensorwerte.lHand == False:
                self.b.getBuecher()

            if self.sensorwerte.lFuss == False:
                #self.t.getTermineToday()
                pass
            if self.sensorwerte.notfall == False:
                pass
                #self.nsms.sendSMS()
            if self.sensorwerte.lOhr == False:
                self.p.getPuls()
        #self.pwr.getPower()
            self.m.getMedikamente()
            #self.t.getTermine()

if __name__ == '__main__':
    m = Main()
    m.callFunctions()





