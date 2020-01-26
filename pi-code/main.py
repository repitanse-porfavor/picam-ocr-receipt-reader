# change directory base imports depending on dev environment
import os
from threading import Thread

import sys
sys.path.append('../')

from buttons.listener import listen_to_btns
from motion.drive_stepper import prepStepper

class PicamOcrReceiptReader:
    def __init__(self):
        self.feedReceipt = False # black button - this manually runs the feed stepper by holding down button
        self.stopAllThreads = False # red button - this is for emergencies
        self.startScan = False # green button - runs automatic scan process after receipt loaded

    def startButtonListenerThread(self):
        Thread(target=listen_to_btns, args=(self,)).start()
    
    def startStepperThread(self):
        Thread(target=prepStepper, args=(self,)).start()

PicamOcr = PicamOcrReceiptReader()
PicamOcr.startButtonListenerThread()
PicamOcr.startStepperThread()