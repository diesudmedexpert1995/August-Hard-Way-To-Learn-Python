people = 40

cars = 12

trucks = 25

if cars > people:
    print("Поедем на машине.")
elif cars < people:
    print("He поедем на машине.")
else:
    print("Мы не можем выбрать.")

if trucks > cars:
    print("Слишком много автобусов.")
elif trucks < cars:
    print("MoжeT, поехать на автобусе?")
else:
    print("Мы до сих пор не можем выбрать.")

if trucks < people:
    print("Хорошо, давайте поедем на автобусе.")
else:
    print("npeKpacHo, давайте останемся дома.")
