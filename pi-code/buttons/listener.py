# note: this code was developed with a Pi Zero W
import sys
# sys.path.append('/home/pi/picam-receipt-reader-ocr/pi-code/states')
# from buttons import load_button_depressed
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO input pins from buttons
RUN_MOTOR_PIN = 16 # black
# RUN_SCAN_PIN = 20  # green
# ABORT_PIN = 21     # red

# setup button input pins with software pull down, fed from 3.3V Pi pin
GPIO.setup(RUN_MOTOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(RUN_SCAN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(ABORT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# while True:
#     print('yo')
#     sleep(80)

def listen_to_btns(self):
    while True:
        run_motor_btn_pressed = GPIO.input(RUN_MOTOR_PIN)
        # run_scan_btn_pressed = GPIO.input(RUN_SCAN_PIN)
        # abort_btn_pressed = GPIO.input(ABORT_PIN)
        
        if (run_motor_btn_pressed):
            self.feedReceipt = True
            print("pressed", run_motor_btn_pressed)
            # break
        else:
            self.feedReceipt = False
            print("pressed", run_motor_btn_pressed)

        # if (run_scan_btn_pressed):

        # if (abort_btn_pressed):

        # print("pressed", run_motor_btn_pressed)

    sleep(80)
    # sleep(1000)

# GPIO.cleanup()