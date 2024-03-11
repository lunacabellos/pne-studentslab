# Exercise 6
from Client0 import Client
from seq import Seq
import os

gene = "FRAT1"
n_fragments = 10
n_bases = 10

print(f"-----| Practice 2, Exercise 6 |------")

IP = "192.168.0.30"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
print(c1)
c2 = Client(IP, PORT2)
print(c2)

filename = os.path.join("..", "sequences", gene + ".txt")
try:
    s = Seq()
    s.read_fasta(filename)
    print(f"Gene {gene}: {s}")

    msg = f"Sending {gene} Gene to the server, in fragments of {n_bases} bases..."
    c1.talk(msg)
    c2.talk(msg)

    start = 0
    end = n_bases
    for i in range(1, n_fragments + 1):
        s_str = str(s)
        fragment = s_str[start:end]
        msg = f"Fragment {i}: {fragment}"
        print(msg)
        if i % 2 != 0:
            c1.talk(msg)
        else:
            c2.talk(msg)

        start += n_bases
        end += n_bases
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")