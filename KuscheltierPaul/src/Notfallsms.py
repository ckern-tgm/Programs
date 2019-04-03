#import gammu
import psycopg2
import re
import os

class Notfallsms(object):

    Name= "Automatischer User"
    Adresse= "Testadresse 23"
    Nummer= "067612345678"

    def __init__(self, conn):
        self.conn = conn

    def getDaten(self):
        cur1 = self.conn.cursor()
        cur2 = self.conn.cursor()
        cur3 = self.conn.cursor()
        SQLName = 'SELECT name FROM kuscheltiernutzer'
        SQLAdr = 'SELECT adresse FROM kuscheltiernutzer'
        SQLTel = 'SELECT tel FROM notfallkontakt'
        cur1.execute(SQLName, )
        cur2.execute(SQLAdr, )
        cur3.execute(SQLTel, )
        row1 = cur1.fetchall()
        row2 = cur2.fetchall()
        row3 = cur3.fetchall()
        for row in row1:
            self.Name = row[0]
        for row in row2:
            self.Adresse = row[0]
        for row in row3:
            self.Nummer = row[0]

        cur1.close()
        cur2.close()
        cur3.close()

    def sendNotfall(self):
        self.getDaten()
        msg = self.Name + ' hat einen Notfall! Adresse: ' + self.Adresse
        with open('notfall.sh','w') as file:
            file.write('echo "'+msg+'" | sudo gammu sendsms TEXT '+self.Nummer)

        os.system('./notfall.sh')

    # def sendNotfall(self):
    #     self.getDaten()
    #     sm = gammu.StateMachine()
    #     sm.ReadConfig()
    #     sm.Init()
    #
    #     msg = {
    #         'Text': self.Name + ' hat einen Notfall! Adresse: ' + self.Adresse,
    #         'SMSC': {'Location': 1},
    #         'Number': '' + self.Nummer
    #     }
    #
    #     sm.SendSMS(msg)


if __name__ == '__main__':
    conn1 = psycopg2.connect("dbname=paul user=vinc password=vinc")
    n = Notfallsms(conn1)
    n.rewrite()
    #n.sendNotfall()