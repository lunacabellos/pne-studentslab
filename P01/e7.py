from Seq1 import *
print("-----| Practice 1, Exercise 7 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")



print(f"Sequence 1: (Length: {s1.len()}): {s1}\n\tBases: {s1.count()}\n\tRev: {s1.reverse()}")
print(f"Sequence 2: (Length: {s2.len()}): {s2}\n\tBases: {s2.count()}\n\tRev: {s2.reverse()}")
print(f"Sequence 3: (Length: {s3.len()}): {s3}\n\tBases: {s3.count()}\n\tRev: {s3.reverse()}")

