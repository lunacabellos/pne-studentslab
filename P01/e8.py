from Seq1 import *
print("-----| Practice 1, Exercise 8 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}): {s1}\n\tBases: {s1.count()}\n\tRev: {s1.reverse()}\n\tComp: {s1.complement()}")
print(f"Sequence 2: (Length: {s2.len()}): {s2}\n\tBases: {s2.count()}\n\tRev: {s2.reverse()}\n\tComp: {s2.complement()}")
print(f"Sequence 3: (Length: {s3.len()}): {s3}\n\tBases: {s3.count()}\n\tRev: {s3.reverse()}\n\tComp: {s3.complement()}")
