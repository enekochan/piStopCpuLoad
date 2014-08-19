# Ref: http://ubuntuforums.org/showthread.php?t=148781
import time
import sys
import RPi.GPIO as GPIO

INTERVAL = 2

R = 18
A = 15
G = 14

def turnOffLights():
    GPIO.output(R, False)
    GPIO.output(A, False)
    GPIO.output(G, False)

def configureGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(A, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    turnOffLights()

def getTimeList():
    statFile = file("/proc/stat", "r")
    timeList = statFile.readline().split(" ")[2:6]
    statFile.close()
    for i in range(len(timeList))  :
        timeList[i] = int(timeList[i])
    return timeList

def deltaTime(interval)  :
    x = getTimeList()
    time.sleep(interval)
    y = getTimeList()
    for i in range(len(x))  :
        y[i] -= x[i]
    return y

if __name__ == "__main__"  :
    configureGPIO()
    while True:
        try:
            dt = deltaTime(INTERVAL)
            cpuPct = 100 - (dt[len(dt) - 1] * 100.00 / sum(dt))
            if cpuPct <= 33:
                GPIO.output(G, True)
                GPIO.output(A, False)
                GPIO.output(R, False)
            elif cpuPct > 33 and cpuPct <= 66:
                GPIO.output(G, False)
                GPIO.output(A, True)
                GPIO.output(R, False)
            else:
                GPIO.output(G, False)
                GPIO.output(A, False)
                GPIO.output(R, True)
        except KeyboardInterrupt:
            turnOffLights()
            sys.exit(0)

