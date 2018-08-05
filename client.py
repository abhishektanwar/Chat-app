import socket
import sys

server_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address=str(sys.argv[1])

port=int(sys.argv[2])

try:
    server_client.connect((ip_address,port))
    print("connected to"+ ip_address+":"+str(port))
except:
    print("failed to connect")
while True:

    incomming_msg=server_client.recv(1024)

    print("SERVER:"+incomming_msg.decode())


    outgoing_msg=input("type your message")
    outgoing_msg=outgoing_msg.encode()
    server_client.send(outgoing_msg)