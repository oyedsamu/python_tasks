# This is a weight converter that can accept either input of kg or lbs
# and changes that into the other.

weight = input("Weight: ")
unit = input("Specify unit (K)g or (L)bs: ")

if unit.upper() == "L":
    print(f"You are {int(weight) * 0.45}kg!")
elif unit.upper()== "K":
    print(f"You are {int(weight) * 2.222}lbs!")
else:
     print(f"Olodo ni e! Does {unit} look like l or k to you?")