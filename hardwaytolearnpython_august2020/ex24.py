print("Давайте попрактикуемся!")
print('Еы должны знать об управляющих последовательностях с символом \\, которые:')
print('\n управляют переносом строк и \t отступами.')
poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\t\tH никогда не отпускать!
"""
print("------------------------------------")
print(poem)
print("------------------------------------")

five = 10-2+3-6

print(f"3дecь должна быть пятерка: {five}")

def secret_formula(started):
    jellybeans = started * 500
    jars = jellybeans / 1000
    crates = jars / 100
    return jellybeans, jars, crates

startpoint = 1000

beans,jars,crates = secret_formula(startpoint)

print("Начиная с: {}".format(startpoint))
print(f"y нас есть {beans} бобов, {jars} банок и {crates} ящиков.")
startpoint = startpoint / 10

print("Мы можем также сделать это таким образом: ")
formula = secret_formula(startpoint)
print("y нас есть {} бобов, {} банок и {} ящиков".format(*formula))
