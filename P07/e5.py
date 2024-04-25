import http.client
import json
import termcolor
from Seq1 import Seq

GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

for gene in GENES:
    SERVER = 'rest.ensembl.org'
    ENDPOINT = "/sequence/id/"
    ID = GENES[gene]
    PARAMS = "?content-type=application/json"
    REQUEST = ENDPOINT + ID + PARAMS
    URL = SERVER + ENDPOINT + ID + PARAMS

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", REQUEST)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received
    response = json.loads(data1)

    termcolor.cprint("Gene: ", 'green', end="")
    print(gene)

    termcolor.cprint("Description: ", 'green', end="")
    print(response['desc'])

    def info_function(s):
        result = f"A: {s.count_base('A')} ({round(s.count_base('A') / s.len() * 100, 1)}%)"
        result += f"\nC: {s.count_base('C')} ({round(s.count_base('C') / s.len() * 100, 1)}%)"
        result += f"\nG: {s.count_base('G')} ({round(s.count_base('G') / s.len() * 100, 1)}%)"
        result += f"\nT: {s.count_base('T')} ({round(s.count_base('T') / s.len() * 100, 1)}%)"
        return result

    s = Seq(response['seq'])

    termcolor.cprint("Total length: ", 'green', end="")
    print(s.len())

    print(info_function(s))

    termcolor.cprint("Most frequent base: ", 'green', end="")
    print(s.max_base())