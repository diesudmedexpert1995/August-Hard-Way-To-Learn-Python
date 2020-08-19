from sys import argv

script, filename = argv
print(f"Я собираюсь стереть файл {filename}.")

print(f"Если вы не хотите стирать его, нажмите сочетание клавиш CTRL+C (^C).")
print("Если хотите стереть файл, нажмите клавишу Enter.")

input("? ")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла. До свидания!")

target.truncate()

print("Teпepь я запрашиваю у вас три строки.")

line1 = input("строка 1:")
line2 = input("строка 2:")
line3 = input("строка 3:")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("Теперь я закрою файл")
target.close()
