import time
from datetime import datetime, timedelta

def checkTime():
    endtime = time.time() +5

    while time.time() < endtime:
        print("hello")
    print(endtime)

# Time in format HOUR:HOUR:MINUTE:MINUTE:SECOND:SECOND
def getTimeHHMMSS():
    return str(datetime.now().time())[0:8]

# time in format HOUR:HOUR:MINUTE:MINUTE
def getTimeHHMM():
    return str(datetime.now().time())[0:5]

# get the weekday of today
def getWeekday():
    return datetime.today().weekday()

# get the current date
def getDate():
    return str(datetime.now().date())

# get date of tmrw.
def getTomorrow():
    return str(datetime.now().date() + timedelta(days=1))

# gets time in HH:MM in 2 hours
def getTimeIn2Hours():
    future_time = datetime.now() + timedelta(hours = 2)
    future_time = future_time.strftime('%H:%M')
    return str(future_time)

# gets Date in 2 hours
def getDateIn2Hours():
    future_time = datetime.now() + timedelta(hours=2)
    future_time = future_time.strftime('%Y-%m-%d')
    return str(future_time)

# get the time of 1 minute ago
def getTime1MinuteAgo():
    past_time = datetime.now() - timedelta(minutes=1)
    past_time = past_time.strftime('%H:%M')
    return str(past_time)


# return the day of the month in length format
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

# Testing only
if __name__ == '__main__':
    checkTime()