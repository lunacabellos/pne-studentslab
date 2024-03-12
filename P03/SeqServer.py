import termcolor

import socket
import os
from Seq1 import Seq


class Server:
    def __init__(self):

        # Configure the Server's IP and PORT
        PORT = 8080
        IP = "127.0.0.1" # it depends on the machine the server is running

        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen()

            while True:
                # accept connections from outside
                print(f"Waiting for clients at {IP}, {PORT}")
                (clientsocket, address) = serversocket.accept()

                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")
                rsp = self.calculate_response(msg)
                print("Message from client: {}".format(msg))

                # Send the message
                send_bytes = str.encode(rsp)
                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()

    def calculate_response(self, msg):
        if msg.startswith("PING"):
            termcolor.cprint("PING command!", "green")
            return "OK!\n"

        elif msg.startswith("GET"):
            termcolor.cprint("GET", 'green')
            get = self.get_function(msg)
            print(get)
            return get

        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", 'green')
            info = self.info_function(msg)
            print(info)
            return info

        elif msg.startswith("COMP"):
            termcolor.cprint("COMP", 'green')
            comp = self.comp_function(msg)
            print(comp)
            return comp

        elif msg.startswith("REV"):
            termcolor.cprint("REV", 'green')
            rev = self.rev_function(msg)
            print(rev)
            return rev

        elif msg.startswith("GENE"):
            gene = self.gene_function(msg)
            print(gene)
            return gene

    def get_function(self, msg):
        which_gene_to_send = msg.split(" ")
        gene_to_send = which_gene_to_send[1]
        genes = ['ADA', 'FRAT1', 'FXN', 'U5', 'RNU6_269P']
        i = 0
        for g in genes:
            if str(i) == gene_to_send:
                seq = Seq(g)
                return seq.read_fasta(g)
            i += 1

    def info_function(self, msg):
        gene = msg.split(" ")
        gene = gene[1]
        seq = Seq(gene)
        length = f"Total length: {seq.len()}"
        c_a = f"\nA:{seq.count_base('A')} ({(seq.count_base('A') / seq.len() * 100):.1f}%)"
        c_c = f"\nC:{seq.count_base('C')} ({(seq.count_base('C') / seq.len() * 100):.1f}%)"
        c_g = f"\nG:{seq.count_base('G')} ({(seq.count_base('G') / seq.len() * 100):.1f}%)"
        c_t = f"\nT:{seq.count_base('T')} ({(seq.count_base('T') / seq.len() * 100):.1f}%)"
        return f"Sequence: {seq} \n{length} {c_a} {c_c} {c_g} {c_t}"

    def comp_function(self, msg):
        seq = msg.split(" ")
        seq = seq[1]
        seq = Seq(seq)
        comp = seq.complement()
        return comp

    def rev_function(self, msg):
        seq = msg.split(" ")
        seq = seq[1]
        seq = Seq(seq)
        rev = seq.reverse()
        return rev

    def gene_function(self, msg):
        which_gene_to_send = msg.split(" ")
        gene = which_gene_to_send[1]
        seq = Seq()
        filename = os.path.join("..", "sequences", gene + ".txt")
        seq.read_fasta(filename)
        return str(seq)


object = Server()