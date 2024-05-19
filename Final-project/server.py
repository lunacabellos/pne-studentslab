import http.server
import socketserver
import http.client
import json
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True
SERVER = 'rest.ensembl.org'
PARAMS = "?content-type=application/json"

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def get_list_species(arguments):
    number = int(arguments['number'][0])

    ENDPOINT = "/info/species/"
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

    ENDPOINT = "/info/assembly/"
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

    try:
        info_chromo = response["karyotype"]
        chromo_list = ""

        for i in info_chromo:
            chromo_list += f"<li>{str(i)}</li>"

        contents = read_html_file('karyotype.html')
        context = {'info_chromo': chromo_list, 'species': species}
        contents = contents.render(context=context)

    except KeyError:
        contents = Path('html/error.html').read_text()

    return contents

def get_length(arguments):
    species = arguments['species'][0]
    chromo = arguments['chromo'][0].upper()

    ENDPOINT = "/info/assembly/"
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
    try:
        length_chromo = None

        for i in response["top_level_region"]:
            if i["name"] == chromo:
                length_chromo = i["length"]

        contents = read_html_file('chrom_length.html')
        context = {'length_chromo': length_chromo, 'species': species, 'chromo': chromo}
        contents = contents.render(context=context)

    except KeyError:
        contents = Path('html/error.html').read_text()

    return contents

def get_id(gene):

    ENDPOINT = "/lookup/symbol/"
    species = "human/"
    REQUEST = ENDPOINT + species + gene.upper() + PARAMS

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
    try:
        id_gene = response["id"]
    except KeyError:
        id_gene = ""
    return id_gene

def get_seq(arguments):
    gene = arguments['gene'][0].upper()
    id_gene = get_id(gene)

    ENDPOINT = "/sequence/id/"
    REQUEST = ENDPOINT + id_gene + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.reason == "Bad Request":
        contents = Path('html/error.html').read_text()
    else:
        data1 = r1.read().decode("utf-8")
        response = json.loads(data1)
        contents = read_html_file('gene_seq.html')
        context = {'gene': gene,  'seq': response["seq"]}
        contents = contents.render(context=context)

    return contents

def get_info(arguments):
    gene = arguments['gene'][0].upper()

    ENDPOINT = "/lookup/symbol/"
    species = "human/"
    REQUEST = ENDPOINT + species + gene + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.reason == "Bad Request":
        contents = Path('html/error.html').read_text()
    else:
        data1 = r1.read().decode("utf-8")
        response = json.loads(data1)
        length = response['end'] - response['start']

        contents = read_html_file('gene_info.html')
        context = {'gene': gene, 'start': response["start"], 'end': response["end"],
                   'length': length,
                   'id': response['id'],
                   'chromo': response['seq_region_name']}
        contents = contents.render(context=context)

    return contents

def get_calc(arguments):
    gene = arguments['gene'][0].upper()
    id_gene = get_id(gene)

    ENDPOINT = "/sequence/id/"
    REQUEST = ENDPOINT + id_gene + PARAMS

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason}\n")

    if r1.reason == "Bad Request":
        contents = Path('html/error.html').read_text()
    else:
        data1 = r1.read().decode("utf-8")
        response = json.loads(data1)
        s = Seq(response["seq"])
        info = ""
        for i in s.count():
            info += f"<li>{i} : {s.count_base(i)} ({round((s.count_base(i) / s.len() * 100), 1)}%)"

        contents = read_html_file('gene_calc.html')
        context = {'gene': gene, 'length': s.len(), 'info': info}
        contents = contents.render(context=context)
    return contents

def get_gene_list(arguments):
    try:
        chromo = arguments['chromo'][0].upper()
        start = arguments['start'][0]
        end = arguments['end'][0]
        print(chromo, start, end)
        ENDPOINT = "/overlap/region/human/"
        NARROW = f"{chromo}:{start}-{end}"
        REQUEST = ENDPOINT + NARROW + PARAMS + ";feature=gene"
        print(REQUEST)
        conn = http.client.HTTPConnection(SERVER)

        try:
            conn.request("GET", REQUEST)
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

        r1 = conn.getresponse()

        print(f"Response received!: {r1.status} {r1.reason}\n")

        if r1.reason == "Bad Request":
            contents = Path('html/error.html').read_text()
        else:
            data1 = r1.read().decode("utf-8")
            response = json.loads(data1)
            genes = ""

            for i in response:
                if "external_name" in i:
                    genes += f"<li>{i['external_name']}</li>"

            if genes == "":
                genes = "No found genes for the selected chromosome interval"

            contents = read_html_file('gene_list.html')
            context = {'chromo': chromo, 'start': start, 'end': end, 'genes': genes}
            contents = contents.render(context=context)
    except KeyError:
        contents = Path('html/error.html').read_text()
    return contents

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

        elif path.startswith("/gene_list"):
            contents = get_gene_list(arguments)

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
