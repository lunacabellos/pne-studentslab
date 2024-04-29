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
print(f"{response}")

print("\n* Testing COMP...")
response = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCATGGAGGAGAGGTCGTTACGGTTGGGGTCAGGTCCGGGGGTAGGCGGGTCCTAGAGCTAGT")
print(f"REV {response}")

print("\n* Testing REV...")
response = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCAACTAGCTCTAGGACCCGCCTACCCCCGGACCTGACCCCAACCGTAACGACCTCTCCTCCA")
print(response)

print("\n* Testing GENE...")
gene = ["U5","ADA", "FRAT1", "FXN", "RNU6_269P"]
for g in gene:
    print(f"GENE {g}")
    response = c.talk(f"GENE {g}")
    print(response)

print("* Testing GET...")
for n in range(5):
    response = c.talk(f"GET {n}")
    print(f"GET {n}: {response}\n")
