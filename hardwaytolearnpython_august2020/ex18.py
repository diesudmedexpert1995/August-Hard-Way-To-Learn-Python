def print_two(*args):
    first, second = args
    print(f"First argument: {first}")
    print(f"Second argument: {second}")


def print_two_again(arg1, arg2):
    print(f"First argument: {arg1}")
    print(f"Second argument: {arg2}")


def print_one(arg1):
    print(f"First argument: {arg1}")


def print_nothing():
    print("I didn`t take any arguments in!!!")


print_two("Vladimir", "Soldatenko")
print_two_again("Vladimir", "Soldatenko")
print_one("Vladimir")
print_nothing()
