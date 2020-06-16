#!/usr/bin/env python

import time
import cec
cec.init()

tv = cec.Device(cec.CECDEVICE_TV)

while True:

    tv.power_on()
    time.sleep(5)
    cec.toggle_mute()
    set_audio_input(10)

    #print(str(tv.is_on()) + "shopuld be true")
    #time.sleep(10)
    #tv.standby()
    #time.sleep(10)
    #print(str(tv.is_on()) + "should be false")
    #time.sleep(10)
