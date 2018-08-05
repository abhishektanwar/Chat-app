import socket
import sys
from _thread import *

server_Server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_Server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

ip=str(sys.argv[1])
port=int(sys.argv[2])
list_of_clients=[]
try:
    server_Server.bind((ip,port))
    print("successfully binded")
except:
    print("binding failed")
    sys.exit()

server_Server.listen(100)
print("server is listening")

def clientthread(conn,addr):
    a = "welcome to chatroom"
    conn.send(a.encode())
    while True:
        incomming_msg=conn.recv(1024)

        print("CLIENT:"+incomming_msg.decode())

        #outgoing_msg=incomming_msg.decode()
        #outgoing_msg=outgoing_msg.encode()
        broadcast(incomming_msg,conn)


def broadcast(message,connection):
    for client in list_of_clients:
        if client != connection :
            client.send(message)

#        for client in list_of_clients:
 #           if client !=addr[1] :
  #              conn.send(outgoing_msg)


while True:
    conn, addr = server_Server.accept()
    list_of_clients.append(conn)

    print(addr[0] + ":" + str(addr[1]) + "connected")
    print(list_of_clients)
    start_new_thread(clientthread,(conn,addr))