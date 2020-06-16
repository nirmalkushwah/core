from req_handler  import *
from ircontrol import *
import json


def load_config():

    with open('device.json') as config_file:
        data = json.load(config_file)
    width = data['module_type']
    height = data['control']
    #print(width)
    #print(height)




if __name__ == "__main__":

    
    make_ser_conn()
    load_config()
    print("hi")
    while True:
        conn, addr = s.accept()
        print("hi")
        print(type(conn))
        print('connected to :' + addr[0]+':'+str(addr[1]))
        start_new_thread(threaded_client,(conn,))


