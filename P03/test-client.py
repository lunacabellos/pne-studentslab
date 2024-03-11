from Client0 import *

print(f"-----| Practice 3, Exercise 7 |------")

PORT = 8080
IP = "127.0.0.1"
c = Client(IP, PORT)
print(c)
print("* Testing PING...")
response = c.talk("PING")
print(response)

print("\n* Testing INFO...")
response = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(f"COMP {response}")

print("\n* Testing COMP...")
response = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCATGGAGGAGAGGTCGTTACGGTTGGGGTCAGGTCCGGGGGTAGGCGGGTCCTAGAGCTAGT")
print(f"REV {response}")

print("\n* Testing REV...")
response = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCAACTAGCTCTAGGACCCGCCTACCCCCGGACCTGACCCCAACCGTAACGACCTCTCCTCCA")
print(response)

print("\n* Testing GENE...")
print("GENE U5")
response = c.talk("GENE U5")
print(response)
print("\nGENE ADA")
response = c.talk("GENE ADA")
print(response)
print("\nGENE FRAT1")
response = c.talk("GENE FRAT1")
print(response)
print("\nGENE FXN")
response = c.talk("GENE FXN")
print(response)
print("\nGENE RNU6_269P")
response = c.talk("GENE RNU6_269P")
print(response)