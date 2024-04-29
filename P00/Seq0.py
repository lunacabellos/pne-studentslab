from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    print("DNA file: ", filename[12:])
    print("The first 20 bases are:\n", list_contents[:20])

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
    print(" ", base, ":", count)

def seq_count(seq):
    dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    FOLDER = "./sequences/"
    FILENAME = seq + ".txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    for i in list_contents:
        dict[i] += 1
    return dict

def seq_reverse(seq, n):
    FOLDER = "./sequences/"
    FILENAME = seq + ".txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    reverse = ''
    seq = list_contents[:n]
    index = len(seq) - 1
    while index >= 0:
        reverse += seq[index]
        index -= 1

    print("Fragment:", seq)
    print("Reverse:", reverse)

def seq_complement(seq):
    FOLDER = "./sequences/"
    FILENAME = seq + ".txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    index = file_contents.find("\n")
    list_contents = (file_contents[index:]).replace("\n", "")
    comp = ''
    seq = list_contents[:20]
    dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    for base in seq:
        comp += dict[base]

    print("Fragment:", seq)
    print("Complement:", comp)


def most_freq_base(seq):
    dict = seq_count(seq)
    list_counts = [dict["A"], dict["C"], dict["G"], dict["T"]]
    max_count = max(list_counts)
    if max_count == dict["T"]:
        print("Gene", seq, ": Most frequent Base: T")
    if max_count == dict["A"]:
        print("Gene", seq, ": Most frequent Base: A")
    if max_count == dict["C"]:
        print("Gene", seq, ": Most frequent Base: C")
    if max_count == dict["G"]:
        print("Gene", seq, ": Most frequent Base: G")
