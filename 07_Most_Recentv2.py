# Get data from user and store it in a list, then
# display the most recent three entries nicely
# Trial #2 - uses a deque method (no need for reverse ordering)

from collections import deque
calculations = deque

# Get five items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

all_calculations.reverse()

# Show that everything made it to the list...
print ()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent 3 ***")
for item in range(0, 3)
    print(all_calculations[item])
