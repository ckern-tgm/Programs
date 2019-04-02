import gammu

class Notfallsms(object):

    def __init__(self, conn):
        self.conn = conn

    def sendNotfall(self, name, adresse, nr):
        sm = gammu.StateMachine()
        sm.ReadConfig()
        sm.Init()

        msg = {
            'Text': name + ' hat einen Notfall! Adresse: ' + adresse,
            'SMSC': {'Location': 1},
            'Number': '' + nr
        }

        sm.SendSMS(msg)