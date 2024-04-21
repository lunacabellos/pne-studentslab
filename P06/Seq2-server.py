import http.server
import os
import socketserver
import termcolor
from pathlib import Path
from Seq0 import seq_reverse, seq_complement, seq_len, seq_count
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

        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        def get_info(sequence):
            text = "Sequence: " + sequence + "<p>" + "Total length: " + str(seq_len(sequence)) + "<p>"
            dict1 = seq_count(sequence)
            for e in dict1:
                index = e + ": "
                percentage = (dict1[e] / seq_len(sequence)) * 100
                percentage = "(" + str(round(percentage, 2)) + "%)"
                text += "<p>" + index + str(dict1[e]) + percentage + "<p>"
            return text

        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        sequences = ["AAACCGTA", "GATA", "AACGT", "CCTGC", "ACGTACGT"]
        keys = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]
        values = []
        for e in keys:
            #filename = "sequences/" + e + ".txt"
            filename = os.path.join("..", "sequences", e + ".txt")
            gene = Path(filename).read_text()
            gene = gene[gene.find("\n"):]
            values.append(gene)
        dict1 = dict(zip(keys, values))

        if path == "/" or path == "/index" or path == "/index.html":
            contents = Path('html/index.html').read_text()

        elif path.startswith("/ping"):
            contents = Path('html/ping.html').read_text()

        elif path.startswith("/get"):
            number = arguments["s"][0]
            text = sequences[int(number)]
            contents = read_html_file("html/get.html").render(context={"todisplay": text})

        elif path.startswith("/gene"):
            key = arguments["g"][0]
            text = dict1[key]
            contents = read_html_file("html/gene.html").render(context={"todisplay": text})

        elif path.startswith("/operation"):
            key = arguments["op"][0]
            if key == "Info":
                text = arguments["operation"][0]
                text2 = "Info"
                text3 = get_info(arguments["operation"][0])
            elif key == "Comp":
                text = arguments["operation"][0]
                text2 = "Comp"
                text3 = seq_complement(arguments["operation"][0])
            else:
                text = arguments["operation"][0]
                text2 = "Rev"
                text3 = seq_reverse(arguments["operation"][0], None)
            contents = read_html_file("html/operation.html").render(
                context={"todisplay": text, "todisplay2": text2, "todisplay3": text3})

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
