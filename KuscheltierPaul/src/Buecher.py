
import platform
import pygame
import psycopg2
import time
import keyboard
import pyttsx3

Directory = "D:/Diplomarbeit/Github/Kuscheltier/Teddy/books/Brueder_Grimm/"
# name = ['Rotkaeppchen', 'Rapunzel', 'Froschkoenig', 'Aschenputtel', 'Gestiefelter_Kater', 'Bremer_Stadtmusikanten', 'Haensel_und_Gretel', 'Goldene_Gans', 'Wilhelm_Tell']
name = []
autor = []
genre = []
pausiert = []
pygame.mixer.init()
FilesPlayed = 0
conn1 = psycopg2.connect("dbname=paul user=Vinc password=Vinc")
engine = pyttsx3.init()




class Buecher(object):

    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "german"
        engine.setProperty('rate', 140)

    engine.setProperty('voice', deutsch)



# Hier werden die Variablen aus dem Parameter der Klasse initialisiert
    def __init__(self, conn, sensorwerte):
        self.conn = conn
        self.sensorwerte = sensorwerte

    def selectBuch(self,conn):

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

    def stopLesen(self):
        pygame.mixer.music.pause()

    def startLesenAgain(self):
        pygame.mixer.music.unpause()


    def getVolume(self):
        #print(pygame.mixer.music.get_volume())
        return pygame.mixer.music.get_volume()

    def volumeUp(self):
        pygame.mixer.music.set_volume(self.getVolume()+0.1)

    def volumeDown(self):
        pygame.mixer.music.set_volume(self.getVolume()-0.1)


    def busy(self,conn,index):
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
            if zeitSeitLetztemSignal>=1:
                try:  # used try so that if user pressed other than the given key error will not be shown
                    if self.sensorwerte.rFuss == False:
                        print(self.getVolume())
                        print('Lauter')
                        self.volumeUp()
                        print(self.getVolume())
                        beginnZeitSeitLetztemSignal = time.time()
                    elif self.sensorwerte.lFuss == False:
                        print(self.getVolume())
                        print('Leiser')
                        self.volumeDown()
                        print(self.getVolume())
                        beginnZeitSeitLetztemSignal = time.time()
                    elif self.sensorwerte.rHand == False:
                        print('Pause')
                        pause_start = time.time()
                        pause = True
                        self.stopLesen()
                        beginnZeitSeitLetztemSignal = time.time()
                    elif self.sensorwerte.lHand == False:
                        print("Lese wieder")
                        elapsed_pause_time = elapsed_pause_time + time.time() - pause_start
                        print("Elapsed Pause Time nach unpause: "+str(elapsed_pause_time))
                        pause = False
                        warSchonPause = True
                        self.startLesenAgain()
                        beginnZeitSeitLetztemSignal = time.time()
                    elif self.sensorwerte.abbr == False:
                        print('Escape')
                        pause_start = time.time()
                        pause = True
                        self.stopLesen()
                        beginnZeitSeitLetztemSignal = time.time()

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
        print(pausiert[index])
        pausiert[index] = elapsed_time + pausiert[index]
        print(pausiert[index])
        data = (pausiert[index], name[index],)
        cur1.execute(SQL_UPDATE_Time, data)
        conn.commit()

    def playSong(self,index):
        #pygame.mixer.music.load(Directory+name[index]+".mp3")
        #pygame.mixer.music.play(1,pausiert[index])
        #busy()
        #pygame.mixer.music.load(Directory + name[index+1] + ".mp3")
        #pygame.mixer.music.play(1, pausiert[index+1])
        #busy()
        print(name)

        #skip = False

        for x in range(index,len(name)):

            for y in range(1):
                engine.say("Wollen sie das Hörbuch" + str(name[x]) + "hören?")
                engine.runAndWait()

                time5 = time.time()+5
                while time.time()<time5:
                    if self.sensorwerte.rHand == False:
                        #skip=True
                        break
                    elif self.sensorwerte.lHand == False:
                        pygame.mixer.music.load(Directory + name[x] + ".mp3")
                        pygame.mixer.music.play(1, pausiert[x])
                        self.busy(conn1, x)
                        #skip = False
                    elif self.sensorwerte.abbr:
                        exit()

                #if skip:
                    #break
        engine.say("Keine Hörbücher mehr übrig. Bitte auf der Webseite neue Hörbücher auswählen.")
        engine.runAndWait()



if __name__ == "__main__":
    conn1 = psycopg2.connect("dbname=paul user=Vinc password=Vinc")
    sensorwerte = 1
    b = Buecher(conn1,sensorwerte)
    b.selectBuch(conn1)
    b.playSong(0)

    pygame.quit()
    print("done")
    exit()