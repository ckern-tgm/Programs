#!/usr/bin/python3
# coding: utf8
#
# @author: Michael Wintersperger <mwintersperger@student.tgm.ac.at>, Simon Appel <sappel@student.tgm.ac.at>
# @version: 20180608
#
# @description: Teddy - the interactive Hedgehog teddy bear client
#
import random
import time
import pyttsx3
import platform

engine = pyttsx3.init()

Englisch = True

# Die Klasse implementiert das Spiel Simon Says. Das Spiel funktioniert wie folgt. Wenn eine Aktion aufgefordert wird, soll diese nur gemacht werden, wenn
# die Worte "Simon sagt " vor der Aktion gesagt wurden.
class SimonSays(object):
    if (platform.system() == 'Windows'):
        deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
        engine.setProperty('rate', 100)
    else:
        deutsch = "mb-de2"
        engine.setProperty('rate', 100)

    englisch = "mb-en1"

    if (Englisch == True):
        engine.setProperty('voice', englisch)
    else:
        engine.setProperty('voice', deutsch)

    engine.setProperty('volume', 1)


    # Hier werden die Variablen aus dem Parameter der Klasse initialisiert
    def __init__(self, conn, sensorwerte):
        self.conn = conn
        self.sensorwerte = sensorwerte


    # Diese Methode gibt in zufälliger Reihenfolge die Ausgabe wieder.
    def getAusgabe(self):
        ausgabe = ""
        zahl = random.randrange(1, 9)
        if zahl == 1:
            ausgabe = "Drücke meine rechte Hand"
        elif zahl == 2:
            ausgabe = "Drücke meine linke Hand"
        elif zahl == 3:
            ausgabe = "Drücke meinen rechten Fuß"
        elif zahl == 4:
            ausgabe = "Drücke meinen linken Fuß"
        elif zahl == 5:
            ausgabe = "Simon sagt drücke meine rechte Hand"
        elif zahl == 6:
            ausgabe = "Simon sagt drücke meine linke Hand"
        elif zahl == 7:
            ausgabe = "Simon sagt drücke meinen rechten Fuß"
        elif zahl == 8:
            ausgabe = "Simon sagt drücke meinen linken Fuß"
        return {
            "ausgabe": ausgabe,
            "zahl": zahl
        }

    # Diese Methode gibt in zufälliger Reihenfolge die Ausgabe wieder.
    def getAusgabeEnglisch(self):
        ausgabe = ""
        zahl = random.randrange(1, 9)
        if zahl == 1:
            ausgabe = "Press my right hand"
        elif zahl == 2:
            ausgabe = "Press my left hand"
        elif zahl == 3:
            ausgabe = "Press my right food"
        elif zahl == 4:
            ausgabe = "Press my left food"
        elif zahl == 5:
            ausgabe = "Simon says press my right hand"
        elif zahl == 6:
            ausgabe = "Simon says press my left hand"
        elif zahl == 7:
            ausgabe = "Simon says press my right food"
        elif zahl == 8:
            ausgabe = "Simon says press my left food"
        return {
            "ausgabe": ausgabe,
            "zahl": zahl
            }


    # Diese Methode identifiziert das Drücken der Knöpfe als Zahl. Wenn z.B. die rechte Hand gedrückt wird, dann wird die Zahl 5 zurück gegeben.
    # Diese Methode wird dafür verwendet, um einen Knopfdruck mit der obig genannten Methode ab zu gleichen. Wenn die Zahl der parseInputs Methode
    # der Zahl der getAusgabe Methode entspricht, ist der gedrückte Knopf richtig.
    def parseInputs(self):
        if self.sensorwerte.rHand == False:
            return 5
        if self.sensorwerte.lHand == False:
            return 6
        if self.sensorwerte.rFuss == False:
            return 7
        if self.sensorwerte.lFuss == False:
            return 8
        return 0

    def falscheAusgabe(self,score):
        if (Englisch == True):
            engine.say('This was wrong')
        else:
            engine.say('Das war leider falsch.')
        engine.runAndWait()
        if (Englisch == True):
            engine.say('You have' + str(score) + 'Points')
        else:
            engine.say('Du hast ' + str(score) + 'Punkte erreicht')
        engine.runAndWait()
        
    def richtigeAusgabe(self):
        if (Englisch == True):
            engine.say('correct')
        else:
            engine.say('richtig')
        engine.runAndWait()
      

    # Diese Methode verwendet die obig genannten Methoden und generiert das Spiel Simon Says.
    # Die Methode überprüft die Zahlen der Methode getAusgabe und vergleicht sie mit den Zahlen der Methode parseInputs
    # Hier befindet sich die Logik des Spiels.
    def getSimonSays(self):
        if (Englisch == True):
            engine.say("You have chosen the game Simon Says")
        else:
            engine.say("Sie haben das Spiel Simon Sagt gewählt")
        engine.runAndWait()
        self.score = 0

        while self.sensorwerte.notfall == False and self.sensorwerte.abbr == True:
            if (Englisch == True):
                ausgabe = self.getAusgabeEnglisch()
            else:
                ausgabe = self.getAusgabe()
            engine.say(ausgabe['ausgabe'])
            engine.runAndWait()
            tend = time.time() + 3
            pressed_something = False

            global input
            input = ""
            
            while time.time() < tend:
                pressed_something = False
                input = self.parseInputs()

                # input obwohl simon says nicht gesagt wurde
                if ausgabe['zahl'] <= 4 and input > 0:
                    self.falscheAusgabe(self.score)
                    self.score = 0
                    pressed_something = True
                    break

                # richtiger Knopf gedrückt, richtige Antwort
                if ausgabe['zahl'] == input:
                    self.richtigeAusgabe()
                    self.score+=1
                    pressed_something = True
                    break

                # Er hat bei Simon Says gedrückt aber es war die falsche Hand
                if ausgabe['zahl'] >= 5 and input >= 5 and input != ausgabe['zahl']:
                    self.falscheAusgabe(self.score)
                    self.score = 0
                    pressed_something = True
                    break

                if self.sensorwerte.abbr == False:
                    break

            if self.sensorwerte.abbr == False:
                if (Englisch == True):
                    engine.say('The game has been stopped')
                else:
                    engine.say('Das Spiel wurde beendet')
                engine.runAndWait()
                break

            # Wenn etwas gedrückt werden soll aber nichts gedrückt wurde
            if ausgabe['zahl'] > 4 and pressed_something == False:
                self.falscheAusgabe(self.score)
                self.score = 0

            #Wenn kein Simon Says gesagt wurde, richtige Antwort
            if(ausgabe['zahl'] <= 4) and pressed_something == False:
                self.richtigeAusgabe()
                self.score += 1

            cur = self.conn.cursor()
            cur.execute("INSERT INTO score VALUES(%s)", (self.score,))
            self.conn.commit
