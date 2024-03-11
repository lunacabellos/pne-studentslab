from Client0 import Client

print(f"-----| Practice 2, Exercise 1 |------")

# -- Parameters of the server to talk to
IP = "212.128.255.64" # the server IP address
PORT = 8081

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()