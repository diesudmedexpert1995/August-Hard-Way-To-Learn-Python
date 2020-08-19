from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read(f))


def rewind(f):
    f.seek(0)


def print_a_line(linecount, f):
    print(linecount, f.readline())

current_file = open(input_file)

print("Firstly, let`s print all file")
print_all(current_file)

print("Firstly, let`s print all file")
rewind(current_file)

current_line = 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 133
print_a_line (current_line, current_file)
