for item in "Samuel":
    print(item + "cool")

for price in range(10, 30, 10):
    total = 0
    total += price
print(f"Total : {total}")

numbers = [2, 2, 2, 2, 10, 10]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)