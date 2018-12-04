from hedgehog.client.sync_client import HedgehogClient
import Medikamente
import Termine
import SimonSays
import Buecher
import Puls
import psycopg2
import Power

rHand = HedgehogClient.get_digital(1)
lHand = HedgehogClient.get_digital(2)
lFuss = HedgehogClient.get_digital(3)
rFuss = HedgehogClient.get_digital(4)
lOhr = HedgehogClient.get_digital(5)
abbr = HedgehogClient.get_digital(6)
notfall = HedgehogClient.get_digital(7)
vibmotor = HedgehogClient.set_digital_output(8,True)

conn = psycopg2.connect("dbname=paul user=Vinc password=Vinc")
m = Medikamente(conn)
t = Termine(conn,rFuss)
s = SimonSays(conn,rHand,lHand,rFuss,lFuss, abbr, notfall)
b = Buecher(conn, rHand)
p = Puls(lOhr)
pwr = Power(vibmotor)

#def t():
    #pass

if __name__ == '__main__':
    s.getSimonSays()
    b.getBuecher()
    p.getPuls()
    #t = Process(target=f, args=('bob',))
    #t.start()
    while True:
        m.getMedikamente()
        t.getTermine()





