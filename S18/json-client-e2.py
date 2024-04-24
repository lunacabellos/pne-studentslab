
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
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
people = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
print("Total people in the database:", len(people["People"]))

for i, dictnum in enumerate(people['People']):
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(people['People'][i]['Firstname'], people['People'][i]['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(people['People'][i]['age'])

    phoneNumbers = people['People'][i]['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i) + ": ", 'blue')
        # The element num contains 2 fields: number and type
        termcolor.cprint("\t Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t Number: ", 'red', end='')
        print(dictnum['number'])