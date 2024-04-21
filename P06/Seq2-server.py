import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import jinja2 as j
from urllib.parse import parse_qs, urlparse


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        filenames = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

        if path == "/" or path == "/index" or path == "/index.html":
            contents = Path('html/index.html').read_text()
        elif path.startswith("/ping"):
            contents = Path('html/ping.html').read_text()
        elif path.startswith("/get"):
            number_seq = int(path.split("=")[1])
            text = [number_seq]
            contents = read_html_file('html/get.html').render(context={"todisplay": text})
        elif path.startswith("/gene"):
            filename = path.strip("/gene?name=")
            if filename in filenames:
                s = Seq()
                s.read_fasta("../sequences/" + filename + ".txt")
                contents = Path("html/gene.html").read_text().format(filename, s)

        elif path.startswith("/operation?seq="):
            ops = path.strip("/operation?").split("&")
            s = Seq()
            s.strbases = ops[0].strip("seq=")
            s.validate()
            if s.valid:
                op = ops[1].strip("op=")
                result = None
                if op == "rev":
                    result = s.reverse()
                elif op == "com":
                    print("hi")
                    result = s.complement()
                elif op == "inf":
                    result = ""
                    result += "Total length: " + str(s.len()) + "<br><br>"
                    count = s.count()
                    for i in count:
                        result += i + ": (" + str(count[i]) + str(
                            round(count[i] / sum([count[j] for j in count]), 1)) + "%)" + "<br>"
                contents = Path("html/operation.html").read_text().format(str(s), op, result)
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
