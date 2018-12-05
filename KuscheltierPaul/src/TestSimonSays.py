import psycopg2
from SimonSays import SimonSays
from pynput import keyboard

rHand = keyboard.Key.down
lHand = keyboard.Key.up
lFuss = keyboard.Key.pause
rFuss = keyboard.Key.alt
lOhr = False
pulsSanalog = False
abbr = False
notfall = False

    # Hier wird die PostgreSQL Verbindung inizialisiert
conn = psycopg2.connect("dbname=paul user=Vinc password=Vinc")

class Main(object):

    def on_press(key):
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if key == keyboard.Key.esc: return False  # stop listener
        if k in ['1', '2', '3', '4', '5', '6', '7']:  # keys interested
            # self.keys.append(k) # store it in global-like variable
            print('Key pressed: ' + k)
            return False  # remove this if want more keys

    lis = keyboard.Listener(on_press=on_press)
    lis.start()  # start to listen on a separate thread
    lis.join()  # no this if main thread is polling self.keys

    s = SimonSays(conn, rHand, lHand, rFuss, lFuss, abbr, notfall)

    s.getSimonSays()