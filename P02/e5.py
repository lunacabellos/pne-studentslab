
from Client0 import Client
from seq import Seq
import os

gene = "FRAT1"
n_fragments = 5
n_bases = 10

print(f"-----| Practice 2, Exercise 5 |------")

IP = "192.168.0.30"
PORT = 8081

c = Client(IP, PORT)
print(c)

filename = os.path.join("..", "sequences", gene + ".txt")
try:
    s = Seq()
    s.read_fasta(filename)
    print(f"Gene {gene}: {s}")

    start = 0
    end = n_bases
    for i in range(1, n_fragments + 1):
        s_str = str(s)
        fragment = s_str[start:end]
        msg = f"Fragment {i}: {fragment}"
        print(msg)
        c.talk(msg)

        start += n_bases
        end += n_bases
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")