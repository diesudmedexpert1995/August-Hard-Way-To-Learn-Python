from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying data from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()
print(f"Input file has length {len(in_data)}")
print(f"Target file is exist : {exists(to_file)}")

print("REady, press Enter to continue or ^C to cancel")

input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Done.")
out_file.close()
in_file.close()
