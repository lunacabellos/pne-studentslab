from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: (Length: {s1.len()}): {s1}\n\tA: {s1.count_base('A')},   C: {s1.count_base('C')},   G: {s1.count_base('G')},   T: {s1.count_base('T')}")
print(f"Sequence 2: (Length: {s2.len()}): {s2}\n\tA: {s2.count_base('A')},   C: {s2.count_base('C')},   G: {s2.count_base('G')},   T: {s2.count_base('T')}")
print(f"Sequence 3: (Length: {s3.len()}): {s3}\n\tA: {s3.count_base('A')},   C: {s3.count_base('C')},   G: {s3.count_base('G')},   T: {s3.count_base('T')}")

