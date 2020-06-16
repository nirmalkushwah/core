
from tvchannel_file import *
from control_file import *
import json 


def feature_Handel(feature_received):
    data = feature_received
    if data["feature"] == "tvchannel":
        tvchannel_Func(feature_received)
        print("tv channel called")
    #if data["feature"] == "light":
        #Func(feature_received)
        #print("light feature called")
    if data["feature"] == "controls":
        controls_Func(feature_received)
        print("Controls called")
