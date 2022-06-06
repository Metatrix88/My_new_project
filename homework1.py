ui1 = int(input("Введите число : "))
ui2 = int(input("Введите число : "))
ui3 = int(input("Введите число : "))
a = ui1 and ui2 and ui3 and "Нет нулевых значений"
print(a)
a = ui1 or ui2 or ui3 or "Введены все нули"
print(a)
if ui1 > (ui2 + ui3):
    print(ui1 - ui2 - ui3)
elif ui1 < (ui2 + ui3):
    print(ui2 + ui3 - ui1)
if ui1 > 50 and (ui2 > ui1 or ui3 > ui1):
    print("Вася")
elif ui1 > 5 or (ui2 == 7 and ui3 == 7):
    print("Петя")
