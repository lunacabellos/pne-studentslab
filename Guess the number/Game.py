
import socket

from Seq1 import Seq


class Server:
    def __init__(self):

        # Configure the Server's IP and PORT
        PORT = 8080
        IP = "127.0.0.1" # it depends on the machine the server is running

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen()

            while True:
                # accept connections from outside
                print(f"Waiting for clients at {IP}, {PORT}")
                (clientsocket, address) = serversocket.accept()

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")
                rsp = self.calculate_response(msg)
                print("Message from client: {}".format(msg))

                # Send the message
                send_bytes = str.encode(rsp)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()


    def calculate_response(self, msg):
        if msg.startswith("PING"):
            termcolor.cprint("PING command!", "green")
            return "OK!\n"