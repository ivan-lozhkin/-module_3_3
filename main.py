def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = ['a', 20.5, False]
values_dict = {'a': 5, 'b': 'int', 'c': True}

values_list_2 = [60.5, 'int']

print_params(1,2,3)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
