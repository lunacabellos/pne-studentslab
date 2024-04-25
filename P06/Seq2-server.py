import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import jinja2 as j
from urllib.parse import parse_qs, urlparse


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

Seqs = ["ACCTG", "GTCACC", "TTACTGAC", "GCGCTAT", "TCCA"]
operations = ["info", "comp", "rev"]


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def get_seq(arguments):
    number = int(arguments['number'][0])
    contents = read_html_file('get.html')
    context = {'number': number, 'sequence': Seqs[number]}
    contents = contents.render(context=context)
    return contents


def get_gene(arguments):
    gene = arguments['name'][0]
    contents = read_html_file('gene.html')
    s = Seq()
    s.read_fasta(gene)
    context = {'name': gene, 'sequence': str(s)}
    contents = contents.render(context=context)
    return contents


def info_function(s):
    result = f"Total length: {s.len()}"
    result += f"<br><br>A: {s.count_base('A')} ({s.count_base('A') / s.len() * 100}%)"
    result += f"<br><br>C: {s.count_base('C')} ({s.count_base('C') / s.len() * 100}%)"
    result += f"<br><br>G: {s.count_base('G')} ({s.count_base('G') / s.len() * 100}%)"
    result += f"<br><br>T: {s.count_base('T')} ({s.count_base('T') / s.len() * 100}%)"
    return result


def get_operation(arguments):
    seq = arguments['seq'][0]
    operation = arguments['operation'][0]
    contents = read_html_file('operation.html')
    s = Seq(seq)
    if operation == "Info":
        result = info_function(s)
    elif operation == "Comp":
        result = s.complement()
    else:
        result = s.reverse()
    context = {'seq': seq, 'operation': operation, 'result': result}
    contents = contents.render(context=context)
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/" or path == "/index" or path == "/index.html":
            contents = Path('html/index.html').read_text()

        elif path.startswith("/ping"):
            contents = Path('html/ping.html').read_text()

        elif path.startswith("/get"):
            contents = get_seq(arguments)

        elif path.startswith("/gene"):
            contents = get_gene(arguments)

        elif path.startswith("/operation"):
            contents = get_operation(arguments)

        else:
            contents = Path('html/error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
socketserver.TCPServer.allow_reuse_address = True

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
