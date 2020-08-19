ten_things = "Яблоки Апельсины Вороны Телефоны Свет Сахар"
print("Погодите, тут меньше 10 объектов. Давайте исправим это.")

stuff = ten_things.split(' ')

more_stuff = ["День", "Банан", "Ночь", "Девочка", "Мишка", "Кукуруза", "Мальчик", "Ночь", "Песня"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"Добавляем: {next_one}")
    stuff.append(next_one)

print("Итак: ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print(''.join(stuff[3:5]))   
