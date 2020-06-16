#from req_handler import *

import threading 
import time 
import sys, getopt 
import json 
import serial 
import signal
from ircontrol import *

#command = {}
#channel_num_list_var = {}
#channel_list_var = {}

def load_driver(device):
    driver = device + ".json"
    print(driver)
    with open('airtel.json') as driver_file:
        driverdata = json.load(driver_file)
    global command
    global channel_num_list_var
    global channel_list_var
    channel_num_list_var = driverdata['channel_num_list']
    channel_list_var = driverdata['channel_list']
    command = driverdata['commands']
    #print(comm['0'])



def load_config():

    with open('device.json') as config_file:
        data = json.load(config_file)
        for doc in data['tv']:
            if doc['room'] == "1":
                 load_driver(doc["make"])
    #print(data['tv'])
    #load_driver(data['tv']['make'])
    #height = data['control']


def tvchannel_Func(feature_received):
    global command
    global channel_num_list_var
    global channel_list_var

    data = feature_received
    
    if "channel_id" in data:
        chann_id = data["channel_id"]
        for i in channel_num_list_var[chann_id]:
            ser_Connect(bytes.fromhex(command[i]))
            time.sleep(.5)
        print("channe called")
    elif "tv_func" in data:
        chann_id = data["tv_func"]
        ser_Connect(bytes.fromhex(command[chann_id]))
        
    else:
        print("Worng Command sent") 
    




load_config()
#3load_driver()

