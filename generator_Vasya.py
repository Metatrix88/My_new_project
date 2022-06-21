def gen_numbers():
    num = 1
    while True:
        if num % 3 != 0:
            yield num
        elif num % 3 == 0:
            yield 'Vasilii'
        num += 1
get_num = gen_numbers()
for i in get_num:
    print(i)
