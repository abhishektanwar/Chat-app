import socket
import sys
from _thread import *

server_Server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_Server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

ip='ABHISHEK'
port=8000
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
        if incomming_msg :


            print("CLIENT:"+incomming_msg.decode())

            outgoing_msg=incomming_msg.decode()
            outgoing_msg=outgoing_msg.encode()
            for client in list_of_clients:
                if client != conn :
                    client.send(outgoing_msg)

        #for client in list_of_clients:
         #   if client !=addr[1] :
          #      conn.send(outgoing_msg)


while True:
    conn, addr = server_Server.accept()
    list_of_clients.append(addr[1])

    print(addr[0] + ":" + str(addr[1]) + "connected")
    print(conn)
    start_new_thread(clientthread,(conn,addr))