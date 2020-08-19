i = 0
numbers = []

while i < 6:
    print(f"The value of counter: {i}. Take it to the list")
    numbers.append(i)

    print(f"The current list: {numbers}")
    i = i + 1
    print(f"The end value i equals {i}")

print("The lists value")

for i in numbers:
    print(f"{i}")
