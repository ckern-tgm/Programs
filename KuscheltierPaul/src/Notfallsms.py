#from __future__ import print_function
import logging
from gsmmodem.modem import GsmModem
#from gsmmodem.modem import Sms

PORT = '/dev/ttyUSB2' #port bei hedgehog angeben
BAUDRATE = 115200
PIN = None # SIM card PIN (if any)


class Notfallsms(object):
    def __init__(self, msg, tel):
        self.msg = msg
        self.tel = tel

    def sendSMS(self):
        #sms = Sms('069917432505', 'Hilfe - Notfall', None)
        modem = GsmModem(PORT, BAUDRATE, None, None, None)
        modem.sendSms(self, self.tel, self.msg, True, 15) #meine nummer zum testen

    def main(self):
        print('Initializing modem...')
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=None)
        print('Sending SMS')
        modem.sendSms(self, self.tel, self.msg, True, 15)  # meine nummer zum testen
        print('SMS sent')

    if __name__ == '__main__':
        main()