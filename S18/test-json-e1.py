import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
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


