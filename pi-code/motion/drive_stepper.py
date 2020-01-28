# referenced:
# https://github.com/custom-build-robots/Stepper-motor-28BYJ-48-Raspberry-Pi/blob/master/decision-maker.py

from time import sleep
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)

# Stepper Pins
IN1 = 6
IN2 = 13
IN3 = 19
IN4 = 26

# waiting time - speed motor turns
time = 0.001

# set GPIO pins
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

# set pins to false
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# 8 steps for 1 full rotation
def Step1():
    GPIO.output(IN4, True)
    sleep (time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep (time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep (time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep (time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

def stepperReverse(steps):
    for i in range(steps):
        Step1()
        Step2()
        Step3()
        Step4()
        Step5()
        Step6()
        Step7()
        Step8()

stepperLastCommandFinished = True
stopStepper = False

# TODO: update for loop with while
def stepperForward(self, steps):
    global stepperLastCommandFinished, stopStepper
    stepperLastCommandFinished = False

    for i in range(steps):
        stopStepper = not(self.feedReceipt)
        # this is bad, lazy code
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step8()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step7()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step6()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step5()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step4()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step3()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step2()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
        Step1()
        if (stopStepper):
            stepperLastCommandFinished = True
            break;
    stepperLastCommandFinished = True
    stopStepper = True


# 512 one rotation

def prepStepper(self):
    global stopStepper, stepperLastCommandFinished
    while True:
        if (self.feedReceipt and stepperLastCommandFinished):
            print('run stepper')
            stopStepper = False
            stepperForward(self, 512)
        if (not(self.feedReceipt)):
            stopStepper = True
        sleep(0.08)


# GPIO.cleanup()