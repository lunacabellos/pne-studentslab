from Client0 import Client
from Seq1 import Seq

genes = ["U5", "FRAT1", "ADA"]

print(f"-----| Practice 2, Exercise 4 |------")

IP = "192.168.0.33"
PORT = 8081

c = Client(IP, PORT)
print(c)

for gene in genes:
    try:
        s = Seq()  # s.__str__()
        s.read_fasta(gene)

        msg = f"Sending {gene} Gene to the server..."
        print(f"To Server: {msg}")
        response = c.talk(msg)
        print(f"From Server: {response}")

        msg = str(s)    # msg = f"{s}" / s.__str__()
        print(f"To Server: {msg}")
        response = c.talk(msg)
        print(f"From Server: {response}")

    except FileNotFoundError:
        print(f"[ERROR]: file ´{gene}´ not found")