sequence= input("Enter a sequence: ")
dic = {"A": 0 ,
       "C": 0 ,
       "G": 0 ,
       "T": 0 }
leng = len(sequence)
for c in sequence:
    if c == "A":
        dic["A"] += 1
    if c == "C":
        dic["C"] += 1
    if c == "G":
        dic["G"] += 1
    if c == "T":
        dic["T"] += 1
    else:
        pass
print("Total length: ", leng, "\n", dic)