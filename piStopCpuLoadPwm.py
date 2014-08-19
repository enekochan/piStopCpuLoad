# Ref: http://pythonhosted.org/RPIO/pwm_py.html
#      http://ubuntuforums.org/showthread.php?t=148781
import time
import RPIO
from RPIO import PWM

INTERVAL = 2

R = 18
A = 15
G = 14

def configureRPIO():
    PWM.set_loglevel(PWM.LOG_LEVEL_ERRORS)
    RPIO.setwarnings(False)
    RPIO.setup(R, RPIO.OUT)
    RPIO.setup(A, RPIO.OUT)
    RPIO.setup(G, RPIO.OUT)
    RPIO.output(R, False)
    RPIO.output(A, False)
    RPIO.output(G, False)

def cleanServo(servo):
    servo.set_servo(G, 1200)
    servo.set_servo(A, 1200)
    servo.set_servo(R, 1200)
    servo.stop_servo(G)
    servo.stop_servo(A)
    servo.stop_servo(R)

def getTimeList():
    statFile = file("/proc/stat", "r")
    timeList = statFile.readline().split(" ")[2:6]
    statFile.close()
    for i in range(len(timeList))  :
        timeList[i] = int(timeList[i])
    return timeList

def deltaTime(interval):
    x = getTimeList()
    time.sleep(interval)
    y = getTimeList()
    for i in range(len(x)):
        y[i] -= x[i]
    return y

if __name__ == "__main__":
    configureRPIO()
    servo = PWM.Servo()
    cleanServo(servo)
    while True:
        dt = deltaTime(INTERVAL)
        cpuPct = 100 - (dt[len(dt) - 1] * 100.00 / sum(dt))
        if cpuPct <= 33:
            servo.set_servo(G, 1200)
            servo.stop_servo(A)
            servo.stop_servo(R)
        elif cpuPct > 33 and cpuPct <= 66:
            servo.stop_servo(G)
            servo.set_servo(A, 1200)
            servo.stop_servo(R)
        else:
            servo.stop_servo(G)
            servo.stop_servo(A)
            servo.set_servo(R, 1200)

