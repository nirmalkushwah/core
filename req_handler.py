import socket
import sys
from _thread import *
import threading
from feature_handler import *

host = ''
port = 5556
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
s.listen(5)


def threaded_client(conn):
    conn.send(str.encode('Welcome, type your data'))
    print(threading.current_thread().name)

    while True:
        #data = conn.recv(2048)
        received_data = json.loads(conn.recv(1024).decode('utf-8'))
        print(received_data)
        feature_Handel(received_data)

    conn.close()

#if __name__ == "__main__":
#    while True:
#        conn, addr = s.accept()
#        print('connected to :' + addr[0]+':'+str(addr[1]))
#        start_new_thread(threaded_client,(conn,))




