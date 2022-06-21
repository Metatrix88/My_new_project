def gen_numbers():
    for num in range(10):
        if num % 3 != 0:
            yield num
        elif num % 3 == 0:
            yield 'Vasilii'
        num += 1


get_num = gen_numbers()
for i in get_num:
    print(i)
