from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    print("DNA file: ", filename[12:])
    print("The first 20 bases are: \n", list_contents[:20])

def seq_len(seq):
    FOLDER = "./sequences/"
    FILENAME = seq + ".txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    print("Gene", seq + "-> Length: ", len(list_contents))

def seq_count_base(seq, base):
    FOLDER = "./sequences/"
    FILENAME = seq + ".txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    count = 0
    for i in list_contents:
        if i == base:
            count += 1
    print(base, ":", count)

def seq_count(seq):
    dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    FOLDER = "./sequences/"
    FILENAME = seq + ".txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i in list_contents:
        if i == "A":
            count_a += 1
        if i == "T":
            count_t += 1
        if i == "G":
            count_g += 1
        if i == "C":
            count_c += 1
    dict["A"] = count_a
    dict["C"] = count_c
    dict["G"] = count_g
    dict["T"] = count_t
    print(dict)
