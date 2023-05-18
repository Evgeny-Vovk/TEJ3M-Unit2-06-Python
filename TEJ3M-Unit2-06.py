# Copyright(c) 2023 Evgeny Vovk All rights reserved.
# Created by : Evgeny Vovk
# Created on : March 2023
# TEJ3M-Unit2-06.py File.

import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP12)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying")
    time.sleep(0.1)
