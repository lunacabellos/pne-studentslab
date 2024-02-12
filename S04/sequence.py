from pathlib import Path

FILENAME = "sequences/Homo_sapiens_ADA_sequence.fa"
file_contents = Path(FILENAME).read_text()
#print(file_contents)

list_contents = file_contents.split("\n")
list_contents.pop(0)
print(len("".join(list_contents)))

#############
index = file_contents.find("\n")
file_contents = (file_contents[index:]).replace("\n","")
print(len(file_contents))