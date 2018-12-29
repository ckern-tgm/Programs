import pyttsx3
import timefile
import platform
import Replace
import psycopg2

# Liefert den Puls zurück
class Medikamente(object):
    engine = pyttsx3.init()

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "german"
        engine.setProperty('rate', 140)

    engine.setProperty('voice', deutsch)

    medikamente = []
    uhrzeiten = []
    anzahl = []
    medikamenteAusgabe = []
    uhrzeitenAusgabe = []
    anzahlAusgabe = []

    #Init Methode zum Setzen der Werte, die man von den Parametern der Klasse bekommt
    def __init__(self, conn):
        self.conn = conn


    def refreshMedikamente(self):

        cur1 = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur3 = self.conn.cursor()

        Wochentag = timefile.getWochentag()
        medikamenteNeu = []
        uhrzeitenNeu = []
        anzahlNeu = []

        # cur.execute("SELECT * FROM medikamente WHERE montag = TRUE;")
        cur1.execute('SELECT name FROM medikamente WHERE %s = TRUE' % (Wochentag,))
        cur2.execute('SELECT zeit FROM medikamente WHERE %s = TRUE' % (Wochentag,))
        cur3.execute('SELECT anz FROM medikamente WHERE %s = TRUE' % (Wochentag,))
        print("The number of Names,Zeit,Anz: ", cur1.rowcount, cur2.rowcount, cur3.rowcount)

        if (cur1.rowcount != cur2.rowcount or cur1.rowcount != cur3.rowcount or cur2.rowcount != cur3.rowcount):
            print("2nd time")
            cur1.execute('SELECT name FROM medikamente WHERE %s = TRUE' % (Wochentag,))
            cur2.execute('SELECT zeit FROM medikamente WHERE %s = TRUE' % (Wochentag,))
            cur3.execute('SELECT anz FROM medikamente WHERE %s = TRUE' % (Wochentag,))

        row1 = cur1.fetchall()
        row2 = cur2.fetchall()
        row3 = cur3.fetchall()
        for row in row1:
            medikamenteNeu.append(row[0])
        for row in row2:
            uhrzeitenNeu.append(row[0].strftime("%H:%M"))
        for row in row3:
            anzahlNeu.append(row[0])

        cur1.close()
        cur2.close()
        cur3.close()
        # conn.close()

        self.medikamente.clear()
        self.uhrzeiten.clear()
        self.anzahl.clear()
        self.medikamenteAusgabe.clear()
        self.uhrzeitenAusgabe.clear()
        self.anzahlAusgabe.clear()

        for i, val in enumerate(medikamenteNeu):
            self.medikamente.append(medikamenteNeu[i])
            self.uhrzeiten.append(uhrzeitenNeu[i])
            self.anzahl.append(anzahlNeu[i])
            # lastTime = conTime
        self.ListeZuAusgabeListe()

    def deleteMedikamente(self,position):
        self.medikamente.pop(position)
        self.uhrzeiten.pop(position)
        self.anzahl.pop(position)

    def ausgabeMedikamente(self,time):
        print("Ausgabe")

        print("Hallo, ich bin es, Paul, es ist")
        self.engine.say("Hallo, ich bin es, Paul, es ist")
        self.engine.runAndWait()

        self.engine.say(Replace.replaceUhrzeit(time))
        self.engine.runAndWait()
        print("[" + Replace.replaceUhrzeit(self.uhrzeitenAusgabe[0]) + "] " + time)
        # uhrzeiten.pop(0)

        self.engine.say("und du musst das Medikament")
        self.engine.runAndWait()
        print("und du musst das Medikament")

        self.engine.say(self.medikamenteAusgabe[0])
        self.engine.runAndWait()
        print(self.medikamenteAusgabe[0])
        # print(medikamente.pop(0))

        self.engine.say(self.anzahlAusgabe[0])
        self.engine.runAndWait()
        # print(anzahl.pop(0))
        print(self.anzahlAusgabe[0])

        self.engine.say("mal nehmen")
        self.engine.runAndWait()
        print("mal nehmen")

    def ListeZuAusgabeListe(self):
        global deleteIndexes
        deleteIndexes = []

        for i, val in enumerate(self.uhrzeiten):
            if (self.uhrzeiten[i] == timefile.getTimeHHMM()):
                print("IN IF")
                self.medikamenteAusgabe.append(self.medikamente[i])
                self.uhrzeitenAusgabe.append(self.uhrzeiten[i])
                self.anzahlAusgabe.append(self.anzahl[i])

                deleteIndexes.append(i)
                # deleteMedikamente(i)
        global deletedElements
        deletedElements = 0
        for i, val in enumerate(deleteIndexes):
            self.deleteMedikamente(deleteIndexes[i] - deletedElements)
            deletedElements = deletedElements + 1
        deletedElements = 0
        deleteIndexes = []

    def MedikamenteMain(self):
        # refreshMedikamente(conn1)
        self.ListeZuAusgabeListe()
        print("Alle Medikamente" + str(self.medikamente))
        print("Ausgabe Medikamente" + str(self.medikamenteAusgabe))
        # refreshMedikamente()
        # print("Alle Medikamente" + str(medikamente))
        # print("Ausgabe Medikamente" + str(medikamenteAusgabe))
        # print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        if (len(self.medikamenteAusgabe) > 0):
            self.ausgabeMedikamente(timefile.getTimeHHMM())

    def getMedikamente(self):
        self.refreshMedikamente()
        self.MedikamenteMain()


if __name__ == '__main__':
    conn1 = psycopg2.connect("dbname=paul user=Vinc password=Vinc")
    m = Medikamente(conn1)
    while True:
        m.getMedikamente()