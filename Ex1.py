my_func = lambda num_1, num_2: num_1/ num_2  
a = int(input())
b = int(input())
if a != 0 and b != 0:
    print(my_func(a,b))
else:
    print('error')