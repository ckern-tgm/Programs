import pyttsx3
import datetime
import platform
from datetime import datetime
import timefile
import Replace
import time
import psycopg2

class Termine(object):

    engine = pyttsx3.init()

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "mb-de2"
        engine.setProperty('rate', 100)

    engine.setProperty('voice', deutsch)

    # global medikamente,uhrzeiten,anzahl,medikamenteAusgabe,uhrzeitenAusgabe,anzahlAusgabe
    termine = []
    uhrzeiten = []
    ort = []
    hinweis = []
    termineAusgabe = []
    uhrzeitenAusgabe = []
    ortAusgabe = []
    hinweisAusgabe = []
    termine24 = []
    uhrzeiten24 = []
    ort24 = []
    hinweis24 = []
    termine2 = []
    uhrzeiten2 = []
    ort2 = []
    hinweis2 = []

    #conn1 = psycopg2.connect("dbname=paul user=Vinc password=Vinc")

    # Init Methode zum Setzen der Werte, die man von den Parametern der Klasse bekommt
    def __init__(self, conn):
        self.conn = conn

    def refreshTermineHeute(self):
        cur1 = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur3 = self.conn.cursor()
        cur4 = self.conn.cursor()
        # cur1.execute("SELECT datum FROM Termine WHERE datum = '2018-11-07';")
        # cur1.execute('SELECT datum FROM Termine WHERE datum = %s' & ("2018-11-07",))
        # cur1.execute('SELECT datum FROM Termine WHERE datum = %s' % ("2018-11-07",))

        SQLDatum = 'SELECT datum FROM Termine WHERE datum = (%s) AND uhrzeit > (%s)'
        SQLUhrzeit = 'SELECT uhrzeit FROM Termine WHERE datum = (%s) AND uhrzeit > (%s)'
        SQLOrt = 'SELECT ort FROM Termine WHERE datum = (%s) AND uhrzeit > (%s)'
        SQLHinweis = 'SELECT hinweis FROM Termine WHERE datum = (%s) AND uhrzeit > (%s)'
        data = (timefile.getDate(), timefile.getTime1MinuteAgo())

        cur1.execute(SQLDatum, data)
        cur2.execute(SQLUhrzeit, data)
        cur3.execute(SQLOrt, data)
        cur4.execute(SQLHinweis, data)

        if (cur1.rowcount != cur2.rowcount or cur1.rowcount != cur3.rowcount or cur1.rowcount != cur4.rowcount or cur2.rowcount != cur3.rowcount or cur2.rowcount != cur4.rowcount or cur3.rowcount != cur4.rowcount):
            cur1.execute(SQLDatum, data)
            cur2.execute(SQLUhrzeit, data)
            cur3.execute(SQLOrt, data)
            cur4.execute(SQLHinweis, data)

        row1 = cur1.fetchall()
        row2 = cur2.fetchall()
        row3 = cur3.fetchall()
        row4 = cur4.fetchall()

        cur1.close()
        cur2.close()
        cur3.close()
        cur4.close()

        self.termine.clear()
        self.uhrzeiten.clear()
        self.ort.clear()
        self.hinweis.clear()
        self.termineAusgabe.clear()
        self.uhrzeitenAusgabe.clear()
        self.ortAusgabe.clear()
        self.hinweisAusgabe.clear()

        # print("Datum: "+ str(Timefile.getDate()))
        for row in row1:
            self.termine.append(row[0].strftime("%Y-%m-%d"))
        for row in row2:
            self.uhrzeiten.append(row[0].strftime("%H:%M"))
        for row in row3:
            self.ort.append(row[0])
        for row in row4:
            self.hinweis.append(row[0])


        self.ListeZuAusgabeListe()


    def refresh24(self):
        cur1 = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur3 = self.conn.cursor()
        cur4 = self.conn.cursor()
        # cur1.execute("SELECT datum FROM Termine WHERE datum = '2018-11-07';")
        # cur1.execute('SELECT datum FROM Termine WHERE datum = %s' & ("2018-11-07",))
        # cur1.execute('SELECT datum FROM Termine WHERE datum = %s' % ("2018-11-07",))

        # 2 hours before

        SQLDatum = 'SELECT datum FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        SQLUhrzeit = 'SELECT uhrzeit FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        SQLOrt = 'SELECT ort FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        SQLHinweis = 'SELECT hinweis FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        # data = ('2018-11-07',)
        data = (timefile.getTomorrow(), timefile.getTimeHHMM(),)

        cur1.execute(SQLDatum, data)
        cur2.execute(SQLUhrzeit, data)
        cur3.execute(SQLOrt, data)
        cur4.execute(SQLHinweis, data)

        if ( cur1.rowcount != cur2.rowcount or cur1.rowcount != cur3.rowcount or cur1.rowcount != cur4.rowcount or cur2.rowcount != cur3.rowcount or cur2.rowcount != cur4.rowcount or cur3.rowcount != cur4.rowcount):
            cur1.execute(SQLDatum, data)
            cur2.execute(SQLUhrzeit, data)
            cur3.execute(SQLOrt, data)
            cur4.execute(SQLHinweis, data)

        row1 = cur1.fetchall()
        row2 = cur2.fetchall()
        row3 = cur3.fetchall()
        row4 = cur4.fetchall()

        self.termine24.clear()
        self.uhrzeiten24.clear()
        self.ort24.clear()
        self.hinweis24.clear()

        # print("Datum: "+ str(Timefile.getDate()))
        for row in row1:
            self.termine24.append(row[0].strftime("%Y-%m-%d"))
        for row in row2:
            self.uhrzeiten24.append(row[0].strftime("%H:%M"))
        for row in row3:
            self.ort24.append(row[0])
        for row in row4:
            self.hinweis24.append(row[0])
        cur1.close()
        cur2.close()
        cur3.close()
        cur4.close()


    def refresh2(self):
        cur1 = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur3 = self.conn.cursor()
        cur4 = self.conn.cursor()
        # cur1.execute("SELECT datum FROM Termine WHERE datum = '2018-11-07';")
        # cur1.execute('SELECT datum FROM Termine WHERE datum = %s' & ("2018-11-07",))
        # cur1.execute('SELECT datum FROM Termine WHERE datum = %s' % ("2018-11-07",))

        # 2 hours before

        SQLDatum = 'SELECT datum FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        SQLUhrzeit = 'SELECT uhrzeit FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        SQLOrt = 'SELECT ort FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        SQLHinweis = 'SELECT hinweis FROM Termine WHERE datum = (%s) AND uhrzeit = (%s)'
        # data = ('2018-11-07',)
        data = (timefile.getDateIn2Hours(), timefile.getTimeIn2Hours(),)

        cur1.execute(SQLDatum, data)
        cur2.execute(SQLUhrzeit, data)
        cur3.execute(SQLOrt, data)
        cur4.execute(SQLHinweis, data)

        if (cur1.rowcount != cur2.rowcount or cur1.rowcount != cur3.rowcount or cur1.rowcount != cur4.rowcount or cur2.rowcount != cur3.rowcount or cur2.rowcount != cur4.rowcount or cur3.rowcount != cur4.rowcount):
            cur1.execute(SQLDatum, data)
            cur2.execute(SQLUhrzeit, data)
            cur3.execute(SQLOrt, data)
            cur4.execute(SQLHinweis, data)

        row1 = cur1.fetchall()
        row2 = cur2.fetchall()
        row3 = cur3.fetchall()
        row4 = cur4.fetchall()

        self.termine2.clear()
        self.uhrzeiten2.clear()
        self.ort2.clear()
        self.hinweis2.clear()

        # print("Datum: "+ str(Timefile.getDate()))
        for row in row1:
            self.termine2.append(row[0].strftime("%Y-%m-%d"))
        for row in row2:
            self.uhrzeiten2.append(row[0].strftime("%H:%M"))
        for row in row3:
            self.ort2.append(row[0])
        for row in row4:
            self.hinweis2.append(row[0])
        cur1.close()
        cur2.close()
        cur3.close()
        cur4.close()


    def getTermineWrong(self):
        return 0


    def setTermine(self,termineNeu, uhrzeitenNeu, ortNeu, hinweisNeu):
        return 0


    def deleteTermine(self,position):
        self.termine.pop(position)
        self.uhrzeiten.pop(position)
        self.ort.pop(position)
        self.hinweis.pop(position)

    def ausgabeTermineJetzt(self,index):



        if (index == 0):
            self.engine.say("Du hast heute")
            self.engine.runAndWait()

            self.engine.say(str(len(self.termine)))
            self.engine.runAndWait()

            self.engine.say("Termine")
            self.engine.runAndWait()

        else:
            self.engine.say("Dein " + str(index + 1) + "ter Termin lautet")
            self.engine.runAndWait()

        self.engine.say("Um")
        self.engine.runAndWait()

        self.engine.say(Replace.replaceUhrzeit(self.uhrzeiten[index]))
        self.engine.runAndWait()

        self.engine.say("musst du in")
        self.engine.runAndWait()

        self.engine.say(self.ort[index])
        self.engine.runAndWait()

        self.engine.say("sein")
        self.engine.runAndWait()

        self.engine.say("Deine Beschreibung zu diesem Termin ist")
        self.engine.runAndWait()

        self.engine.say(self.hinweis[index])
        self.engine.runAndWait()


    def ausgabe24(self,index):
        self.engine.say("Morgen, um")
        self.engine.runAndWait()

        self.engine.say(Replace.replaceUhrzeit(self.uhrzeiten24[index]))
        self.engine.runAndWait()

        self.engine.say("musst du in")
        self.engine.runAndWait()

        self.engine.say(self.ort24[index])
        self.engine.runAndWait()

        self.engine.say("sein")
        self.engine.runAndWait()

        self.engine.say("Deine Beschreibung zu diesem Termin ist")
        self.engine.runAndWait()

        self.engine.say(self.hinweis24[index])
        self.engine.runAndWait()


    def ausgabe2(self,index):
        self.engine.say("Um")
        self.engine.runAndWait()

        self.engine.say(Replace.replaceUhrzeit(self.uhrzeiten2[index]))
        self.engine.runAndWait()

        self.engine.say("musst du in")
        self.engine.runAndWait()

        self.engine.say(self.ort2[index])
        self.engine.runAndWait()

        self.engine.say("sein")
        self.engine.runAndWait()

        self.engine.say("Deine Beschreibung zu diesem Termin ist")
        self.engine.runAndWait()

        self.engine.say(self.hinweis2[index])
        self.engine.runAndWait()


    def ListeZuAusgabeListe(self):
        global deleteIndexes
        deleteIndexes = []

        for i, val in enumerate(self.uhrzeiten):
            if (self.uhrzeiten[i] == timefile.getTimeHHMM()):
                self.termineAusgabe.append(self.termine[i])
                self.uhrzeitenAusgabe.append(self.uhrzeiten[i])
                self.ortAusgabe.append(self.ort[i])
                self.hinweisAusgabe.append(self.hinweis[i])

                deleteIndexes.append(i)
                # deleteMedikamente(i)
        global deletedElements
        deletedElements = 0
        for i, val in enumerate(deleteIndexes):
            self.deleteTermine(deleteIndexes[i] - deletedElements)
            deletedElements = deletedElements + 1
        deletedElements = 0
        deleteIndexes = []


    def ausgabeAlleTermine(self):
        if len(self.termine)==0:
            print("Keine heutigen Termine")
            self.engine.say("Du hast heute keine Termine")
            self.engine.runAndWait()
        else:

            for i, val in enumerate(self.termine):
                self.ausgabeTermineJetzt(i)



    def ausgabeAlle24(self):
        for i, val in enumerate(self.termine24):
            self.ausgabe24(i)


    def ausgabeAlle2(self):
        for i, val in enumerate(self.termine2):
            self.ausgabe2(i)


    def TermineMain(self):
        # refreshTermine(conn1)
        self.ListeZuAusgabeListe()
        # refreshMedikamente()
        # print("Alle Termine" + str(termine))
        # print("Ausgabe Termine" + str(termineAusgabe))
        # print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        if (len(self.termineAusgabe) > 0):
            return 0

    def getTermine(self):
        self.refresh2()
        self.ausgabeAlle2()

        self.refresh24()
        self.ausgabeAlle24()

    def getTermineHeute(self):
        self.refreshTermineHeute()
        self.ausgabeAlleTermine()

if __name__ == "__main__":
    conn1 = psycopg2.connect("dbname=paul user=vinc password=vinc")
    t = Termine(conn1)

    t.getTermineHeute()
    print(t.getTermineHeute())

    #t.refreshTermineHeute()
    # while True:
    #   refreshTermine(conn1)
    #    TermineMain()
    #t.ausgabeAlleTermine()

    while True:
        t.getTermine()

