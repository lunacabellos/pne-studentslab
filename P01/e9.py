
# Exercise 9
import os
from Seq1 import *

print(f"-----| Practice 1, Exercise 9 |------")

# -- Create a Null sequence
s = Seq()

GENE = "U5"

filename = os.path.join("..", "sequences", GENE + ".txt")
try:
    s.read_fasta(filename)
    print(f"Sequence: (Length: {s.len()}) {s}")
    print(f"\tBases: {s.count()}")
    print(f"\tRev:  {s.reverse()}")
    print(f"\tComp: {s.complement()}")
except FileNotFoundError:
    print(f"[ERROR]: file ´{filename}´ not found")
