def read_dicts_from_data(filename):

    list_of_dicts = []

    with open(filename, "r", encoding="latin-1") as f:

        header = next(f).replace("\n", "").split(",")

        for line in f:

            components = line.replace("\n", "").split(",")

            d = dict(zip(header, components))

            list_of_dicts.append(d)

    return list_of_dicts
dna_count_file = read_dicts_from_data("dna_count_file.txt")

sequence= input("Enter a sequence: ")
dic = {"A": 0 ,
       "C": 0 ,
       "G": 0 ,
       "T": 0 }
n_of_bases = len(sequence)
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
print("Number of bases: ", n_of_bases, "\n", dic)