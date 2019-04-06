import pyttsx3
import timefile
import platform
import Replace
import psycopg2

Englisch = True

# Klasse Medikamente
# Simon Appel
class Medikamente(object):

    # init speech engine
    engine = pyttsx3.init()

    # set language drive depending on os
    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "mb-de2"
        engine.setProperty('rate', 100)

    englisch = "english"

    # set englisch or german
    if (Englisch == True):
        engine.setProperty('voice', englisch)
    else:
        engine.setProperty('voice', deutsch)

    engine.setProperty('volume', 1)

    # class arrays
    medikamente = []
    uhrzeiten = []
    anzahl = []
    # Elements in Ausgabe are going to be spoken
    medikamenteAusgabe = []
    uhrzeitenAusgabe = []
    anzahlAusgabe = []

    #Init Methode zum Setzen der Werte, die man von den Parametern der Klasse bekommt
    def __init__(self, conn):
        self.conn = conn

    # refreshMedikamente gets Medikamente out of the DB and puts them into the class arrays
    def refreshMedikamente(self):

        cur1 = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur3 = self.conn.cursor()

        Wochentag = timefile.getWochentag()
        medikamenteNeu = []
        uhrzeitenNeu = []
        anzahlNeu = []

        # Get only certain medicine which should be said today
        # cur.execute("SELECT * FROM medikamente WHERE montag = TRUE;")
        cur1.execute('SELECT name FROM medikamente WHERE %s = TRUE' % (Wochentag,))
        cur2.execute('SELECT zeit FROM medikamente WHERE %s = TRUE' % (Wochentag,))
        cur3.execute('SELECT anz FROM medikamente WHERE %s = TRUE' % (Wochentag,))

        if (cur1.rowcount != cur2.rowcount or cur1.rowcount != cur3.rowcount or cur2.rowcount != cur3.rowcount):
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

        # clear all Medikamente which are currently in the system
        self.medikamente.clear()
        self.uhrzeiten.clear()
        self.anzahl.clear()
        self.medikamenteAusgabe.clear()
        self.uhrzeitenAusgabe.clear()
        self.anzahlAusgabe.clear()

        # put Medikamente from this method to class arrays
        for i, val in enumerate(medikamenteNeu):
            self.medikamente.append(medikamenteNeu[i])
            self.uhrzeiten.append(uhrzeitenNeu[i])
            self.anzahl.append(anzahlNeu[i])
            # lastTime = conTime
        # check and add Medikamente into the Ausgabe Arrays, if they should be announced right now
        self.ListeZuAusgabeListe()

    # delete Medikamente at a certain position
    def deleteMedikamente(self,position):
        self.medikamente.pop(position)
        self.uhrzeiten.pop(position)
        self.anzahl.pop(position)

    # this method announced the Medikamente
    def ausgabeMedikamente(self,time):

        if (Englisch == True):
            self.engine.say("Hello, it's me, Paul. It is")
        else:
            self.engine.say("Hallo, ich bin es, Paul, es ist")
        self.engine.runAndWait()

        self.engine.say(Replace.replaceUhrzeit(time))
        self.engine.runAndWait()
        # uhrzeiten.pop(0)

        if (Englisch == True):
            self.engine.say("and you have to take the medication")
        else:
            self.engine.say("und du musst das Medikament")
        self.engine.runAndWait()

        self.engine.say(self.medikamenteAusgabe[0])
        self.engine.runAndWait()

        self.engine.say(self.anzahlAusgabe[0])
        self.engine.runAndWait()

        if (Englisch == True):
            self.engine.say("times")
        else:
            self.engine.say("mal nehmen")
        self.engine.runAndWait()

    # this method puts the Medikamente from the class array into the Ausgabe Array
    def ListeZuAusgabeListe(self):
        global deleteIndexes
        deleteIndexes = []

        # this for method adds the Medikamente into the Liste
        for i, val in enumerate(self.uhrzeiten):
            if (self.uhrzeiten[i] == timefile.getTimeHHMM()):
                self.medikamenteAusgabe.append(self.medikamente[i])
                self.uhrzeitenAusgabe.append(self.uhrzeiten[i])
                self.anzahlAusgabe.append(self.anzahl[i])

                deleteIndexes.append(i)
                # deleteMedikamente(i)

        global deletedElements
        deletedElements = 0
        # this for method deletes the Medikamente which shouldnt be in their anymore
        for i, val in enumerate(deleteIndexes):
            self.deleteMedikamente(deleteIndexes[i] - deletedElements)
            deletedElements = deletedElements + 1
        deletedElements = 0
        deleteIndexes = []

    # this method calls the Class to Ausgabe Array checker and also the ausgabeMedikamente function to announce the Medikamente
    def MedikamenteMain(self):
        # refreshMedikamente(conn1)
        self.ListeZuAusgabeListe()
        # refreshMedikamente()
        # print("Alle Medikamente" + str(medikamente))
        # print("Ausgabe Medikamente" + str(medikamenteAusgabe))
        # print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        if (len(self.medikamenteAusgabe) > 0):
            self.ausgabeMedikamente(timefile.getTimeHHMM())

    # combine refresh and MedikamenteMain to 1 Method to be called from the main class
    def getMedikamente(self):
        self.refreshMedikamente()
        self.MedikamenteMain()

# Testing purpose only
if __name__ == '__main__':
    conn1 = psycopg2.connect("dbname=paul user=vinc password=vinc")
    m = Medikamente(conn1)
    while True:
        m.getMedikamente()
