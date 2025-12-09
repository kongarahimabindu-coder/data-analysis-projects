food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.

food_list = food.split(",")
equipment_list = equipment.split(",")
pets_list = pets.split(",")
sleep_aids_list = sleep_aids.split(",")

food_list.sort()
equipment_list.sort()
pets_list.sort()
sleep_aids_list.sort()

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = []
cargo_hold.append(food_list)
cargo_hold.append(equipment_list)
cargo_hold.append(pets_list)
cargo_hold.append(sleep_aids_list)
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

cabinet_value = int(input("select a cabinet (0-3):"))

if cabinet_value <= 3:
    print("I selected cabinet", cabinet_value)
    print("contents:", cargo_hold[cabinet_value])
else:
    print("Invalid selection. please choose a number from 0 to 3.")
# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

if cabinet_value <= 3:
    print("cabinet {} contains: {}".format(cabinet_value, cargo_hold[cabinet_value]))
else:
    print("Error: {} is not valid cabinet number. Please enter 0-3.".format(cabinet_value))

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

cabinet__for_both = int(input("select a cabinet (0-3):"))

if cabinet__for_both <= 3:
    print("Cabinet {} contains: {}".format(cabinet__for_both, cargo_hold[cabinet__for_both]))

    item = input("Enter the item you are looking for: ")

    if item in cargo_hold[cabinet__for_both]:
        print("Cabinet {} DOES contain '{}'.".format(cabinet__for_both, item))
    else:
        print("Cabinet {} DOES NOT contain '{}'.".format(cabinet__for_both, item))
else:
    print("Error: {} is not a valid cabinet number. Please enter 0–3.".format(cabinet__for_both))