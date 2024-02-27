class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            count = 0
            for e in strbases:
                if e == "A" or e == "C" or e == "G" or e == "T":
                    count += 1
            if count == len(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = "ERROR"
                print("INVALID sequence!")
    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        self.base = base
        if self.strbases is None or base not in self.strbases:
            return 0
        else:
            return self.strbases.count(base)

    def count(self):
        dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        for i in self.strbases:
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
        return dict

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "ERROR"
        else:
            reverse = ''
            seq = self.strbases
            index = len(seq) - 1
            while index >= 0:
                reverse += seq[index]
                index -= 1
            return reverse

    def complement(self):
        complement = ""
        if self.strbases == None:
            return "NULL"
        else:
            for base in self.strbases:
                if base == "A":
                    complement += "T"
                elif base == "G":
                    complement += "C"
                elif base == "C":
                    complement += "G"
                elif base == "T":
                    complement += "A"
                else:
                    return "ERROR"
        return complement

    def read_fasta(self, filename):
        self.filename = filename
        file_content = Path(filename).read_text()
        lines = file_content.splitlines()
        body = lines[1:]
        dna_sequence = ""
        for line in body:
            dna_sequence += line
        return dna_sequence

    def read_fasta(self, filename):
        with open(filename, "r") as f:
            file_contents = Path(filename).read_text()
            list_contents = file_contents.split("\n")
            complete_seq = ""
            for i in range(1, len(list_contents)):
                complete_seq += (list_contents[i])
            f.close()
        return complete_seq




