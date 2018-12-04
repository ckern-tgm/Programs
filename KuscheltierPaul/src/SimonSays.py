#!/usr/bin/python3
# coding: utf8
#
# @author: Michael Wintersperger <mwintersperger@student.tgm.ac.at>, Simon Appel <sappel@student.tgm.ac.at>
# @version: 20180608
#
# @description: Teddy - the interactive Hedgehog teddy bear client
#
import random
import pyttsx3

engine = pyttsx3.init()

class SimonSays(object):
	def __init__(self, conn,rHand,lHand,rFuss,lFuss, abbr, notfall):
		self.conn = conn
		self.rHand = rHand
		self.lHand = lHand
		self.rFuss = rFuss
		self.lFuss = lFuss
		self.abbr = abbr
		self.notfall = notfall


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
			ausgabe = "Simon says drücke meine rechte Hand"
		elif zahl == 6:
			ausgabe = "Simon says drücke meine linke Hand"
		elif zahl == 7:
			ausgabe = "Simon says drücke meinen rechten Fuß"
		elif zahl == 8:
			ausgabe = "Simon says drücke meinen linken Fuß"
		return {
			"ausgabe": ausgabe,
			"zahl": zahl
		}

	def parseInputs(self):
		if self.rHand:
			return 5
		if self.lHand:
			return 6
		if self.rFuss:
			return 7
		if self.lFuss:
			return  8





	def getSimonSays(self):
		engine.say("Sie haben das Spiel Simon Says gewählt")
		engine.runAndWait()
		score = 0
		while self.notfall == False and self.abbr == False:
			ausgabe = self.getAusgabe()
			engine.say(ausgabe['ausgabe'])
			engine.runAndWait()

			if ausgabe['zahl'] <= 4:
				engine.say('Das war leider falsch.')
				engine.runAndWait()
				engine.say('Dein Score beträgt '+str(score))
			elif ausgabe['zahl'] == self.parseInputs():
				engine.say('richtig')
				engine.runAndWait()
				score += 1
		cur = self.conn.cursor()
		cur.execute("INSERT INTO score VALUES(%s)", (score,))
		self.conn.commit