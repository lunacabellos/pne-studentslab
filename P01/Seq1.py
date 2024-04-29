from pathlib import Path

class Seq:
    bases = ["A", "G", "C", "T"]
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

        for i in self.strbases:
            if self.strbases is None or i not in dict:
                pass
            else:
                dict[i] += 1
        return dict

    def reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
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
        dict_comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
        complement = ""
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        else:
            for base in self.strbases:
                complement += dict_comp[base]
            return complement

    def read_fasta(self, filename):
        folder = "../sequences/"
        filename = filename + ".txt"
        file_contents = Path(folder + filename).read_text()
        header = file_contents.find("\n")
        body = file_contents[header:]
        list_contents = body.replace("\n", "")
        self.strbases = list_contents
        return self.strbases

    def max_base(self):
        bases_dict = {}
        for b in Seq.bases:
            bases_dict[b] = self.count_base(b)

        most_frequent_base = max(bases_dict, key=bases_dict.get)

        return most_frequent_base

    def processing(self, gene):
        dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for g in gene:
            dict[g] += 1
        biggest_value = 0
        answer = ""
        for keys in dict:
            if biggest_value < dict[keys]:
                biggest_value = dict[keys]
                answer = keys
        return answer



