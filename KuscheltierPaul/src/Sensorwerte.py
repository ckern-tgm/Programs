from hedgehog.client import connect
from threading  import Thread
import time


class Sensorwerte():

    def __init__(self):
        Thread(target=self.update).start()
        self.rHand = True
        self.lHand = True
        self.lFuss = True
        self.rFuss = True
        self.pulsAnalog = True
        self.lOhr = True
        self.notfall = True
        self.abbr = True

    def update(self):
        with connect(process_setup=False) as hedgehog:
            while True:
                hedgehog.set_input_state(0,True)
                self.rHand = hedgehog.get_digital(0)
                hedgehog.set_input_state(1,True)
                self.lHand = hedgehog.get_digital(1)
                hedgehog.set_input_state(2,True)
                self.rFuss = hedgehog.get_digital(2)
                hedgehog.set_input_state(3,True)
                self.lFuss = hedgehog.get_digital(3)
                hedgehog.set_input_state(4,True)
                self.lOhr = hedgehog.get_digital(4)
                self.pulsAnalog = hedgehog.get_analog(4)
                hedgehog.set_input_state(6,True)
                self.abbr = hedgehog.get_digital(6)
                hedgehog.set_input_state(7,True)
                self.notfall = hedgehog.get_digital(7)
                time.sleep(0.1) 
