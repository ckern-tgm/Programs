#import alsaaudio
import platform
import pygame
from pygame.locals import *
import psycopg2
import time
import keyboard
import pyttsx3

# path where all books are stored
global Directory
Directory = "/home/pi/Programs/KuscheltierPaul/books/Brueder_Grimm/"


# name = ['Rotkaeppchen', 'Rapunzel', 'Froschkoenig', 'Aschenputtel', 'Gestiefelter_Kater', 'Bremer_Stadtmusikanten', 'Haensel_und_Gretel', 'Goldene_Gans', 'Wilhelm_Tell']
# arrays which are used in this class
name = []
autor = []
genre = []
pausiert = []
pygame.mixer.init()
FilesPlayed = 0
#conn1 = psycopg2.connect("dbname=paul user=Vinc password=Vinc")
engine = pyttsx3.init()
#m = alsaaudio.Mixer()
#vol = m.getVolume()
#print(vol)

Englisch = True

class Buecher(object):

    # set language drive depending on os
    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)

        Directory = "D:/Diplomarbeit/Github/Kuscheltier/Teddy/books/Brueder_Grimm/"
    else:
        deutsch = "mb-de2"
        engine.setProperty('rate', 100)
        Directory = "/home/pi/Programs/KuscheltierPaul/books/Brueder_Grimm"

    englisch = "english"

    # set langauge german or english
    if (Englisch == True):
        engine.setProperty('voice', englisch)
    else:
        engine.setProperty('voice', deutsch)

    engine.setProperty('volume', 1)


# Hier werden die Variablen aus dem Parameter der Klasse initialisiert
    def __init__(self, conn, sensorwerte):
        self.conn = conn
        self.sensorwerte = sensorwerte

    # this method gets all books which are checked on the website
    def selectBuch(self,conn):
        
        print(self.sensorwerte.rHand)
        
        cur1 = conn.cursor()
        cur2 = conn.cursor()
        cur3 = conn.cursor()
        cur4 = conn.cursor()

        SQLName = 'SELECT name FROM Buch WHERE ausgewaehlt = TRUE'
        SQLAutor = 'SELECT autor FROM Buch WHERE ausgewaehlt = TRUE'
        SQLGenre = 'SELECT genre FROM Buch WHERE ausgewaehlt = TRUE'
        SQLPausiert = 'SELECT pausiert FROM Buch WHERE ausgewaehlt = TRUE'

        cur1.execute(SQLName, )
        cur2.execute(SQLAutor, )
        cur3.execute(SQLGenre, )
        cur4.execute(SQLPausiert, )

        if (
                cur1.rowcount != cur2.rowcount or cur1.rowcount != cur3.rowcount or cur1.rowcount != cur4.rowcount or cur2.rowcount != cur3.rowcount or cur2.rowcount != cur4.rowcount or cur3.rowcount != cur4.rowcount):
            cur1.execute(SQLName, )
            cur2.execute(SQLAutor, )
            cur3.execute(SQLGenre, )
            cur4.execute(SQLPausiert, )

        row1 = cur1.fetchall()
        row2 = cur2.fetchall()
        row3 = cur3.fetchall()
        row4 = cur4.fetchall()

        for row in row1:
            name.append(row[0])
        for row in row2:
            autor.append(row[0])
        for row in row3:
            genre.append(row[0])
        for row in row4:
            pausiert.append(row[0])

        cur1.close()
        cur2.close()
        cur3.close()
        cur4.close()

    # stop reading a mp3-File
    def stopLesen(self):
        pygame.mixer.music.pause()

    # start the reading again
    def startLesenAgain(self):
        pygame.mixer.music.unpause()

    # get the curent volume
    def getVolume(self):
        #print(pygame.mixer.music.get_volume())
        return pygame.mixer.music.get_volume()

    # turn up the current volume
    def volumeUp(self):
        pygame.mixer.music.set_volume(self.getVolume()+0.1)

    # turn down the current volume
    def volumeDown(self):
        pygame.mixer.music.set_volume(self.getVolume()-0.1)

    # this method lets the mp3-File play until its over.
    # it also checks if some buttons are hit for calling stop, etc.
    def busy(self,conn,index):
        print("in busy")
        cur1 = conn.cursor()
        SQL_UPDATE_Time = 'UPDATE Buch SET pausiert = (%s) WHERE name = (%s)'
        start_time = time.time()
        elapsed_time = 0
        pause = False
        warSchonPause = False
        global elapsed_pause_time
        elapsed_pause_time = 0
        global pause_start
        global pause_end

        zeitSeitLetztemSignal = 1
        beginnZeitSeitLetztemSignal = 0
        # while mp3 file is being played
        while pygame.mixer.music.get_busy() == True:

            #KeyboardSignalZeit

            print("Zeit der Pausen: "+str(elapsed_pause_time))

            print(start_time)
            if pause == False and warSchonPause == False:
                elapsed_time = time.time() - start_time # + pausiert[0]
            if pause == False and warSchonPause == True:
                elapsed_time = time.time() - start_time - elapsed_pause_time

            zeitSeitLetztemSignal = time.time() - beginnZeitSeitLetztemSignal

            print(elapsed_time)
            # check if last button hit is > 1 sec. ago
            # check for button hits and call actions
            if zeitSeitLetztemSignal>=1:
                try:  # used try so that if user pressed other than the given key error will not be shown
                    # Hit rechter fuss
                    if self.sensorwerte.rFuss == False:
                        print(self.getVolume())
                        print('Lauter')
                        self.volumeUp()
                        print(self.getVolume())
                        beginnZeitSeitLetztemSignal = time.time()
                    # hit linker fuss
                    elif self.sensorwerte.lFuss == False:
                        print(self.getVolume())
                        print('Leiser')
                        self.volumeDown()
                        print(self.getVolume())
                        beginnZeitSeitLetztemSignal = time.time()
                    # hit rechte hand
                    elif self.sensorwerte.rHand == False:
                        print('Pause')
                        pause_start = time.time()
                        pause = True
                        self.stopLesen()
                        beginnZeitSeitLetztemSignal = time.time()
                    # hit linke hand
                    elif self.sensorwerte.lHand == False:
                        print("Lese wieder")
                        elapsed_pause_time = elapsed_pause_time + time.time() - pause_start
                        print("Elapsed Pause Time nach unpause: "+str(elapsed_pause_time))
                        pause = False
                        warSchonPause = True
                        self.startLesenAgain()
                        beginnZeitSeitLetztemSignal = time.time()
                    # hit abbrechen button
                    elif self.sensorwerte.abbr == False:
                        print('Escape')
                        pause_start = time.time()
                        pause = True
                        self.stopLesen()
                        beginnZeitSeitLetztemSignal = time.time()

                        # commit the time it has played into the db to start reading from this position again
                        print(pausiert[index])
                        pausiert[index] = elapsed_time + pausiert[index]
                        print(pausiert[index])
                        data = (pausiert[index], name[index],)
                        cur1.execute(SQL_UPDATE_Time, data)
                        conn.commit()
                        break

                    else:
                        pass
                except:
                    pass  # if user pressed a key other than the given key the loop will break
                #schonGesendet=True
                #continue

        # commit the played time
        print(pausiert[index])
        pausiert[index] = elapsed_time + pausiert[index]
        print(pausiert[index])
        data = (pausiert[index], name[index],)
        cur1.execute(SQL_UPDATE_Time, data)
        conn.commit()

    # this method calls the (next) song
    # after 5 seconds or rechte Hand it asks for listening the next book
    def playSong(self,index):
        #pygame.mixer.music.load(Directory+name[index]+".mp3")
        #pygame.mixer.music.play(1,pausiert[index])
        #busy()
        #pygame.mixer.music.load(Directory + name[index+1] + ".mp3")
        #pygame.mixer.music.play(1, pausiert[index+1])
        #busy()
        print(name)

        #skip = False

        global abbr
        abbr = False

        print("In Play Song")

        for x in range(index,len(name)):
            if abbr:
                break
            for y in range(1):
                if abbr:
                    break
                if (Englisch == True):
                    engine.say("Do you want to listen to" + str(name[x]))
                else:
                    engine.say("Wollen sie das Hörbuch" + str(name[x]) + "hören?")
                engine.runAndWait()

                time5 = time.time()+5
                while time.time()<time5:
                    print(str(time5))
                    print(str(time.time()))
                    print("In while")
                    # ask next book
                    if self.sensorwerte.rHand == False:
                        print("rechte hand break")
                        #skip=True
                        break
                    # play chosen book
                    elif self.sensorwerte.lHand == False:
                        print(Directory+name[x]+".mp3")
                        pygame.mixer.music.load(Directory + name[x] + ".mp3")
                        pygame.mixer.music.play(1, pausiert[x])
                        self.busy(self.conn, x)
                        #skip = False
                    # get out of the reading function, back to the main class
                    elif self.sensorwerte.abbr == False:
                        abbr = True
                        break

                #if skip:
                    #break
        # after listinting to every possible book
        if abbr==False:
            if (Englisch == True):
                engine.say("No books available. Please choose more books on the website.")
            else:
                engine.say("Keine Hörbücher mehr übrig. Bitte auf der Webseite neue Hörbücher auswählen.")
            engine.runAndWait()
        else:
        # after getting out of the book function back to the main class
            abbr=False
            if (Englisch == True):
                engine.say("Book listening has ended")
            else:
                engine.say("Hörbuch vorlesen wurde beendet.")
            engine.runAndWait()

    # this method gets called from the main class
    # it class the method for getting the books and playing them
    def getBuecher(self):
        print("Vor select Buch")
        self.selectBuch(self.conn)
        print("vor abspielen")
        self.playSong(0)

# Testing purpose only
if __name__ == "__main__":
    conn1 = psycopg2.connect("dbname=paul user=vinc password=vinc")
    sensorwerte = 1
    b = Buecher(conn1,sensorwerte)
    b.selectBuch(conn1)
    b.playSong(0)

    pygame.quit()
    print("done")
    exit()
