def int_func():
    my_str = input()
    my_str.split
    for word in my_str:
        s = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                s = s + 1
        if s == len(word):
            print(word.title())
        else:
            print('только латиница')
    pass
print('введите строку')
int_func()