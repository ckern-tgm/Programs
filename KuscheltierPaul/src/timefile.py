import time
from datetime import datetime, timedelta

def checkTime():
    endtime = time.time() +5

    while time.time() < endtime:
        print("hello")
    print(endtime)

def getTimeHHMMSS():
    return str(datetime.now().time())[0:8]

def getTimeHHMM():
    return str(datetime.now().time())[0:5]

def getWeekday():
    return datetime.today().weekday()

def getDate():
    return str(datetime.now().date())

def getTomorrow():
    return str(datetime.now().date() + timedelta(days=1))

def getTimeIn2Hours():
    future_time = datetime.now() + timedelta(hours = 2)
    future_time = future_time.strftime('%H:%M')
    return str(future_time)

def getDateIn2Hours():
    future_time = datetime.now() + timedelta(hours=2)
    future_time = future_time.strftime('%Y-%m-%d')
    return str(future_time)

def getTime1MinuteAgo():
    past_time = datetime.now() - timedelta(minutes=1)
    past_time = past_time.strftime('%H:%M')
    return str(past_time)



Wochentag = ""
def getWochentag():
    global Wochentag
    if(getWeekday()==0):
        Wochentag = "montag"
    if (getWeekday() == 1):
        Wochentag = "dienstag"
    if (getWeekday() == 2):
        Wochentag = "mittwoch"
    if (getWeekday() == 3):
        Wochentag = "donnerstag"
    if (getWeekday() == 4):
        Wochentag = "freitag"
    if (getWeekday() == 5):
        Wochentag = "samstag"
    if (getWeekday() == 6):
        Wochentag = "sonntag"

    return Wochentag

if __name__ == '__main__':
    checkTime()