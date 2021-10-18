def func(x, y):
    c = x
    for i in range(1, abs(y)):
        x = x * c
    x = 1 / x
    print('x в степени y =', x)
    pass
print('введите x')
x = int(input())
print('введите y')
y = int(input())
func(x, y)