import socket
import termcolor
from Client0 import Client

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.88" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening, server ready to listen different request
ls.listen()

print("The server is configured!")

i = 1
while True:
    (rs, address) = ls.accept()
    print("Waiting for Clients to connect")
    print(f"A client has connected to the server!")
    Msg = f"CONNECTION {i}. Client IP,PORT: {address}"
    rs.send(Msg.encode())
    msg = rs.recv(2048).decode("utf-8")
    print("Message received: " + termcolor.colored(msg, "green"))
    newMsg = "\nECHO:  " + msg
    rs.send(newMsg.encode())
    rs.close()
    i += 1
# -- Close the socket
ls.close()