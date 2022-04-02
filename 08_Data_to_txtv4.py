# Source: https://www.guru99.com/reading-and-writing-files-in-python.html
# Includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a Filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            probelm = "(no spaces allowed"

        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    else:
        print("You entered a valid filename")
