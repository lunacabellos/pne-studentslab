from pathlib import Path

FILENAME = "sequences/Homo_sapiens_RNU6_1155P_sequence.fa"
file_contents = Path(FILENAME).read_text()
print(file_contents)