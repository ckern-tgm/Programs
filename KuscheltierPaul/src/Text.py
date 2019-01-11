from hedgehog.client import connect

def setPort():
    with connect() as hedgehog:
        rHand = hedgehog.get_digital(1)
        hedgehog.set_input_state(1,True)
