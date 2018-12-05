import time

def checkTime():
    endtime = time.time() +5

    while time.time() < endtime:
        print("hello")
    print(endtime)

if __name__ == '__main__':
    checkTime()