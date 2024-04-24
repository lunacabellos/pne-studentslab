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

SERVER = 'rest.ensembl.org'
ENDPOINT = "/sequence/id/"
INPUT_NAME = input("Write the gene name:")
INPUT_ID = GENES[INPUT_NAME]
PARAMS = "?content-type=application/json"
REQUEST = ENDPOINT + INPUT_ID + PARAMS
URL = SERVER + ENDPOINT + INPUT_ID + PARAMS

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
print(INPUT_NAME)

termcolor.cprint("Description: ", 'green', end="")
print(response['desc'])

s = Seq(response['seq'])

termcolor.cprint("Total length: ", 'green', end="")
print(s.len())