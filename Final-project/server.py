import http.server
import socketserver
import http.client
import json
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def get_list_species(arguments):
    number = int(arguments['number'][0])

    SERVER = 'rest.ensembl.org'
    ENDPOINT = "/info/species/"
    PARAMS = "?content-type=application/json"
    REQUEST = ENDPOINT + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)

    list_species = response["species"][:number]
    name_list = ""

    for i in list_species:
        name_list += f"<li>{i['display_name']}</li>"

    total_species = len(response["species"])
    contents = read_html_file('species.html')
    context = {'number': number, 'total': total_species, 'list_species': name_list}
    contents = contents.render(context=context)
    return contents

def get_karyotype(arguments):
    species = arguments['species'][0]

    SERVER = 'rest.ensembl.org'
    ENDPOINT = "/info/assembly/"
    PARAMS = "?content-type=application/json"
    REQUEST = ENDPOINT + species + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)

    info_chromo = response["karyotype"]
    chromo_list = ""

    for i in info_chromo:
        chromo_list += f"<li>{str(i)}</li>"

    contents = read_html_file('karyotype.html')
    context = {'info_chromo': chromo_list, 'species': species}
    contents = contents.render(context=context)
    return contents

def get_length(arguments):
    species = arguments['species'][0]
    chromo = arguments['chromo'][0].upper()

    SERVER = 'rest.ensembl.org'
    ENDPOINT = "/info/assembly/"
    PARAMS = "?content-type=application/json"
    REQUEST = ENDPOINT + species + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    length_chromo = None

    for i in response["top_level_region"]:
        if i["name"] == chromo:
            length_chromo = i["length"]

    contents = read_html_file('chrom_length.html')
    context = {'length_chromo': length_chromo, 'species': species, 'chromo': chromo}
    contents = contents.render(context=context)
    return contents

def get_id(gene):

    SERVER = 'rest.ensembl.org'
    ENDPOINT = "/lookup/symbol/"
    species = "human/"
    PARAMS = "?expand=1;content-type=application/json"
    REQUEST = ENDPOINT + species + gene + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    response1 = json.loads(data1)
    id_gene = response1["id"]
    return id_gene

def get_seq(arguments):
    gene = arguments['gene'][0].upper()
    id_gene = get_id(gene)

    SERVER = 'rest.ensembl.org'
    ENDPOINT = "/sequence/id/"
    PARAMS = "?content-type=text/plain"
    REQUEST = ENDPOINT + id_gene + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    data1 = r1.read().decode("utf-8")
    gene_seq = json.loads(data1)

    contents = read_html_file('gene_seq.html')
    context = {'gene': gene,  'seq': gene_seq}
    contents = contents.render(context=context)
    return contents

def get_info(arguments):
    pass

def get_calc(arguments):
    pass

def get_genelist(arguments):
    pass

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/" or path == "/index" or path == "/index.html":
            contents = Path('html/index.html').read_text()

        elif path.startswith("/list"):
            contents = get_list_species(arguments)

        elif path.startswith("/karyotype"):
            contents = get_karyotype(arguments)

        elif path.startswith("/length"):
            contents = get_length(arguments)

        elif path.startswith("/seq"):
            contents = get_seq(arguments)

        elif path.startswith("/info"):
            contents = get_info(arguments)

        elif path.startswith("/calc"):
            contents = get_calc(arguments)

        elif path.startswith("/genelist"):
            contents = get_genelist(arguments)

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


socketserver.TCPServer.allow_reuse_address = True

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
