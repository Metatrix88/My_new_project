from datetime import datetime
import os
import time

zero = ["⬛⬜⬜⬜⬜⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬜⬜⬜⬜⬛"]

one = ["⬛⬛⬛⬜⬛⬛⬛",
       "⬛⬛⬜⬜⬛⬛⬛",
       "⬛⬛⬛⬜⬛⬛⬛",
       "⬛⬛⬛⬜⬛⬛⬛",
       "⬛⬛⬛⬜⬛⬛⬛",
       "⬛⬛⬛⬜⬛⬛⬛",
       "⬛⬛⬜⬜⬜⬛⬛"]

two = ["⬛⬜⬜⬜⬜⬜⬛",
       "⬛⬛⬛⬛⬛⬜⬛",
       "⬛⬛⬛⬛⬜⬛⬛",
       "⬛⬛⬛⬜⬛⬛⬛",
       "⬛⬛⬜⬛⬛⬛⬛",
       "⬛⬜⬛⬛⬛⬛⬛",
       "⬛⬜⬜⬜⬜⬜⬛"]

three = ["⬛⬜⬜⬜⬜⬜⬛",
         "⬛⬛⬛⬛⬛⬜⬛",
         "⬛⬛⬛⬛⬛⬜⬛",
         "⬛⬛⬜⬜⬜⬜⬛",
         "⬛⬛⬛⬛⬛⬜⬛",
         "⬛⬛⬛⬛⬛⬜⬛",
         "⬛⬜⬜⬜⬜⬜⬛"]

four = ["⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬜⬜⬜⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛"]

five = ["⬛⬜⬜⬜⬜⬜⬛",
        "⬛⬜⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬛⬛⬛⬛",
        "⬛⬜⬜⬜⬜⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛",
        "⬛⬜⬜⬜⬜⬜⬛"]

six = ["⬛⬜⬜⬜⬜⬜⬛",
       "⬛⬜⬛⬛⬛⬛⬛",
       "⬛⬜⬛⬛⬛⬛⬛",
       "⬛⬜⬜⬜⬜⬜⬛",
       "⬛⬜⬛⬛⬛⬜⬛",
       "⬛⬜⬛⬛⬛⬜⬛",
       "⬛⬜⬜⬜⬜⬜⬛"]

seven = ["⬛⬜⬜⬜⬜⬜⬛",
         "⬛⬛⬛⬛⬛⬜⬛",
         "⬛⬛⬛⬛⬛⬜⬛",
         "⬛⬛⬛⬛⬜⬛⬛",
         "⬛⬛⬛⬜⬛⬛⬛",
         "⬛⬛⬜⬛⬛⬛⬛",
         "⬛⬜⬛⬛⬛⬛⬛"]

eight = ["⬛⬜⬜⬜⬜⬜⬛",
         "⬛⬜⬛⬛⬛⬜⬛",
         "⬛⬜⬛⬛⬛⬜⬛",
         "⬛⬜⬜⬜⬜⬜⬛",
         "⬛⬜⬛⬛⬛⬜⬛",
         "⬛⬜⬛⬛⬛⬜⬛",
         "⬛⬜⬜⬜⬜⬜⬛"]

nine = ["⬛⬜⬜⬜⬜⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬛⬛⬛⬜⬛",
        "⬛⬜⬜⬜⬜⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛",
        "⬛⬛⬛⬛⬛⬜⬛",
        "⬛⬜⬜⬜⬜⬜⬛"]

separator_one = ["⬛⬛⬛",
                 "⬛⬜⬛",
                 "⬛⬜⬛",
                 "⬛⬛⬛",
                 "⬛⬜⬛",
                 "⬛⬜⬛",
                 "⬛⬛⬛"]


separator_two = ["⬛⬛⬛",
                 "⬛⬛⬛",
                 "⬛⬛⬛",
                 "⬛⬛⬛",
                 "⬛⬛⬛",
                 "⬛⬛⬛",
                 "⬛⬛⬛"]

dct = {'0': zero,
       '1': one,
       '2': two,
       '3': three,
       '4': four,
       '5': five,
       '6': six,
       '7': seven,
       '8': eight,
       '9': nine,
       ':': separator_one,
       ';': separator_two}

y = 0
while True:
    def flicker():
        if y % 2 == 0:
            yield datetime.now().strftime("%H:%M:%S")
        elif y % 2 == 1:
            yield datetime.now().strftime("%H;%M;%S")
    string = flicker()
    string = next(string)
    watch = []
    for x in string:
        if x in dct.keys():
            watch.append(dct[x])
    print(watch[0][0] + watch[1][0] + watch[2][0] + watch[3][0] + watch[4][0] + watch[5][0] + watch[6][0] + watch[7][0])
    print(watch[0][1] + watch[1][1] + watch[2][1] + watch[3][1] + watch[4][1] + watch[5][1] + watch[6][1] + watch[7][1])
    print(watch[0][2] + watch[1][2] + watch[2][2] + watch[3][2] + watch[4][2] + watch[5][2] + watch[6][2] + watch[7][2])
    print(watch[0][3] + watch[1][3] + watch[2][3] + watch[3][3] + watch[4][3] + watch[5][3] + watch[6][3] + watch[7][3])
    print(watch[0][4] + watch[1][4] + watch[2][4] + watch[3][4] + watch[4][4] + watch[5][4] + watch[6][4] + watch[7][4])
    print(watch[0][5] + watch[1][5] + watch[2][5] + watch[3][5] + watch[4][5] + watch[5][5] + watch[6][5] + watch[7][5])
    print(watch[0][6] + watch[1][6] + watch[2][6] + watch[3][6] + watch[4][6] + watch[5][6] + watch[6][6] + watch[7][6])
    y += 1
    time.sleep(1)
    os.system('cls')
