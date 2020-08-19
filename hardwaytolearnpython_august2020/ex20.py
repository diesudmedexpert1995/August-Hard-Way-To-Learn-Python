def add(a, b):
    print(f"Addition {a}+{b}")
    return a+b


def subtract(a, b):
    print(f"Subtraction {a}-{b}")
    return a-b


def multiply(a,b):
    print(f"Multyply {a}*{b}")
    return a*b


def divide(a,b):
    print(f"Divide {a}/{b}")
    return a/b


age = add(20, 5)
height = subtract(190, 4)
weight = multiply(24, 3)
iq = divide(300, 3)
print(f"Возраст: {age}, Рост: {height}, Bec: {weight}, IQ: {iq}")

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what = age+(height-(weight*(iq/2)))
print(what)
