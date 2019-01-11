from hedgehog.client import connect
class x(object):
    self.rHand = True
    def updateValues(self):
        while True:
            self.rHand = hedgehog.get_digital(1)
            hedgehog.set_input_state(1,True)

if __name__ == '__main__':
    x = x()
    while True:
        print(self.rHand)
        x.updateValues()
