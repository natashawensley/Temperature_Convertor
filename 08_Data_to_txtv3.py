# Source: https://www.guru99.com/reading-and-writing-files-in-python.html
# Includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)

import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename (leave off the extension): ")

valid_file = "[A-Zaz]"
if re.match(valid_file, filename):
    # add txt.suffix
    filename = filename + ".txt"

    # Create file to hold data
    f = open(filename, "w+")

    # Add new line at end of each item
    for item in data:
        f.write(item + "\n")

    # Close file
    f.close()

else:
    print("oops!")
