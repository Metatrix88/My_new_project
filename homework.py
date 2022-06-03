from tkinter import Menu

height = float(input("Введите свой рост в см: "))
weight = float(input("Введите свой вес в кг: "))
age = int(input("Введите свой возраст: "))
height = height/100 #Переводим в метры

if age < 10 or age > 100 or height < 0 or height > 300 or weight < 0 or weight > 300:
    print("Некоректно введены данные")
bmi = weight / (height * height)
bmi = round(bmi)

gender = input("Введите свой пол, (м/ж): ")

if gender == "ж":
    if age < 50 and bmi <= 20:
        print("Ваш BMI равен", bmi, "пол женский, это означает, что у вас недостаточный вес.")
    elif age < 50 and bmi > 20 and bmi <= 30:
        print("Ваш BMI равен", bmi, "пол женский, это означает, что у вас все в норме,красотка!")
    elif age < 50 and bmi > 30 and bmi <= 40:
        print("Ваш BMI равен", bmi, "пол женский, это означает, что пора в спорт зал!")
    elif age > 50 and bmi >= 16 and bmi <= 30:
        print("Ваш BMI равен", bmi, "пол женский, это означает, что у вас все в норме,шикарная женщина!")
    elif age > 50 and bmi > 30 and bmi <= 40:
        print("Ваш BMI равен", bmi, "пол женский, это означает, что у вас избыточный вес,ноги в руги - шагом марш!!!")
    else:
        print("Обратитесь к специалисту!!!")
else:
    if gender == "м":
        if age < 50 and bmi <= 20:
            print("Ваш BMI равен", bmi, "пол мужской, это означает, что надо больше кушать.")
        elif age < 50 and bmi > 20 and bmi <= 30:
            print("Ваш BMI равен", bmi, "пол мужской, это означает, что у вас все в норме, молоток!")
        elif age < 50 and bmi > 30 and bmi <= 40:
            print("Ваш BMI равен", bmi, "пол мужской, это означает, что ты лентяй и не занимаешься собой!")
        elif age > 50 and bmi >= 16 and bmi <= 30:
            print("Ваш BMI равен", bmi, "пол мужской, это означает, что у вас все в норме,так держать!")
        elif age > 50 and bmi > 30 and bmi <= 40:
            print("Ваш BMI равен", bmi, "пол мужской, это означает, что вам надо больше шагать вокруг дома")
        else:
            print("Ты приплыл, the end!!!")

l1 = bmi - 16
l2 = 40 - bmi
str1 = l1 * "="
str2 = l2 * "="
print(f'16{str1}|{str2}40')
