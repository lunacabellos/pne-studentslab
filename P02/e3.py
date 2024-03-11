from Client0 import Client

print(f"-----| Practice 2, Exercise 3 |------")
IP = "10.1.153.180"
PORT = 8081
c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")