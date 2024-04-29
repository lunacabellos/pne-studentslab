
from Client0 import Client
from Seq1 import Seq

gene = "FRAT1"
n_fragments = 5
n_bases = 10

print(f"-----| Practice 2, Exercise 5 |------")

IP = "192.168.0.30"
PORT = 8081

c = Client(IP, PORT)
print(c)

try:
    s = Seq()
    s.read_fasta(gene)
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
    print(f"[ERROR]: file '{gene}' not found")