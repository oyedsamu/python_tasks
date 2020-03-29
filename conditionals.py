# Conditionals
name = input("What is name? ")
if len(name) < 3:
    print(f"{name} is too short na abeg!")
elif len(name) > 50:
    print(f"{name[:4]}... may not be a name bayen, you sure say no be sentence?")
else:
    print(f"{name} is just perfect!")