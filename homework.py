height = float(input("Enter your height in sm:"))
weight = float(input("Enter your weight in kg:"))
height = height/100 #Переводим в метры
if height < 0 or height > 300 or weight < 0 or weight > 300:
    print("Please try again")
bmi = weight / (height * height)
bmi = round(bmi)
 print("Your body mass index is:", bmi)

l1 = bmi - 16
l2 = 40 - bmi
str1 = l1 * "="
str2 = l2 * "="
print(f'16{str1}|{str2}40')
