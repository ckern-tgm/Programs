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

# Die Klasse implementiert das Spiel Simon Says. Das Spiel funktioniert wie folgt. Wenn eine Aktion aufgefordert wird, soll diese nur gemacht werden, wenn
# die Worte "Simon sagt " vor der Aktion gesagt wurden.
class SimonSays(object):
	if (platform.system() == 'Windows'):
		deutsch = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\eSpeak_3"
		engine.setProperty('rate', 100)
	else:
		deutsch = "german"
		engine.setProperty('rate', 140)

	engine.setProperty('voice', deutsch)
	# Hier werden die Variablen aus dem Parameter der Klasse initialisiert
	def __init__(self, conn,rHand,lHand,rFuss,lFuss, abbr, notfall):
		self.conn = conn
		self.rHand = rHand
		self.lHand = lHand
		self.rFuss = rFuss
		self.lFuss = lFuss
		self.abbr = abbr
		self.notfall = notfall

	# Diese Methode gibt in zufälliger Reihenfolge die Ausgabe wieder.
	def getAusgabe(self):
		ausgabe = ""
		zahl = random.randrange(1,9)
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


	# Diese Methode identifiziert das Drücken der Knöpfe als Zahl. Wenn z.B. die rechte Hand gedrückt wird, dann wird die Zahl 5 zurück gegeben.
	# Diese Methode wird dafür verwendet, um einen Knopfdruck mit der obig genannten Methode ab zu gleichen. Wenn die Zahl der parseInputs Methode
	# der Zahl der getAusgabe Methode entspricht, ist der gedrückte Knopf richtig.
	def parseInputs(self):
		if self.rHand:
			return 5
		if self.lHand:
			return 6
		if self.rFuss:
			return 7
		if self.lFuss:
			return  8
		return 0





	def falscheAusgabe(self,score):
			engine.say('Das war leider falsch.')
			engine.runAndWait()
			engine.say('Dein Score beträgt '+str(score))
			engine.runAndWait()

	# Diese Methode verwendet die obig genannten Methoden und generiert das Spiel Simon Says.
	# Die Methode überprüft die Zahlen der Methode getAusgabe und vergleicht sie mit den Zahlen der Methode parseInputs
	# Hier befindet sich die Logik des Spiels.
	def getSimonSays(self):
		engine.say("Sie haben das Spiel Simon Says gewählt")
		engine.runAndWait()
		score = 0
		while self.notfall == False and self.abbr == False:
			ausgabe = self.getAusgabe()
			engine.say(ausgabe['ausgabe'])
			engine.runAndWait()
			tend = time.time()+5
			while time.time() < tend:
				if ausgabe['zahl'] <= 4 and self.parseInputs() > 0:
					engine.say('Das war leider falsch.')
					engine.runAndWait()
					engine.say('Dein Score beträgt '+str(score))
					engine.runAndWait()

				elif (ausgabe['zahl'] <= 4) and (self.parseInputs() == 0):
					engine.say('richtig.')
					engine.runAndWait()
				elif ausgabe['zahl'] == self.parseInputs():
					engine.say('richtig')
					engine.runAndWait()
					score += 1
				else:
					self.falscheAusgabe(score)

		cur = self.conn.cursor()
		cur.execute("INSERT INTO score VALUES(%s)", (score,))
		self.conn.commit