print('символ завершающий программу - s')
print('start')
def play():
    sum_num = 0
    while True:
        str_of_num = input()
        str_of_num = str_of_num.split()
        for i in str_of_num:
            if i.lower() == 's':
                return print(sum_num, 'game over')
            else:
                sum_num = sum_num + int(i)
        print (sum_num)
    pass
print(play())