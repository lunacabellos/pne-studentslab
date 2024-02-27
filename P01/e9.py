from pathlib import Path
from Seq1 import *
print("-----| Practice 1, Exercise 9 |------")

FOLDER = "./sequences/"
FILENAME = "sequences/U5.txt"
full_filename = Path(FOLDER) / FILENAME
s1 = Seq()
s1.read_fasta(FILENAME)

print(f"Sequence 1: (Length: {s1.len()}): {s1}\n\tBases: {s1.count()}\n\tRev: {s1.reverse()}\n\tComp: {s1.complement()}")




