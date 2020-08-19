# поключаем из модуля sys компонент для получения значений из входящей строки
from sys import argv

# получаем первым значением название нашей программи, вторым - название файла для чтения
script, filename = argv

# открываем файл для чтения
txt = open(filename, "r")

# Выводим строку с названием файла
print(f"Inside the file: {filename}")

# получаем содержимое файла на вывод
print(txt.read())
txt.close()

# Следующие четыре строки  абсолютно идентичны, так как мы выводим содержимое указанного второго файла
print("Enter the file name once more: ")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
