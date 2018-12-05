from hedgehog.client.sync_client import HedgehogClient
from hedgehog.client import connect
from Medikamente import Medikamente
from Termine import Termine
from SimonSays import SimonSays
from Buecher import Buecher
from Puls import Puls
import psycopg2
from Power import Power

# Die Main Klasse ist die, die alle Klassen zusammen bringt und deren Funktionen verwendet. Hier befinden sich alle Funktionen des Kuscheltiers.
class Main(object):

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
    conn = psycopg2.connect("dbname=paul user=Vinc password=Vinc")

    # Hier werden Objekte der benötigten Klassen erstellt
    m = Medikamente(conn)
    t = Termine(conn,rFuss)
    s = SimonSays(conn,rHand,lHand,rFuss,lFuss, abbr, notfall)
    b = Buecher(conn, rHand)
    p = Puls(lOhr, pulsSanalog)
    pwr = Power()

    #def thread():
        #pass
    # Die Methode ruft alle benötigten Funktionen der Klassen auf
    def callFunctions(self):
        self.pwr.getPower()
        self.s.getSimonSays()
        self.b.getBuecher()
        self.p.getPuls()
        #thread = Process(target=f, args=('bob',))
        #thread.start()
        while True:
            self.m.getMedikamente()
            self.t.getTermine()


# Hier wird die Methode callFunctions ausgeführt.
if __name__ == '__main__':
    m = Main()
    m.callFunctions()





