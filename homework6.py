my_dict = {'Yaroslav': 1995, 'Grant': 1997, 'Elena': 1991}
print(my_dict)
print(my_dict['Grant'])
print(my_dict.get('lex'))
my_dict['Anastasiya'] = 2001
my_dict['Max'] = 1999
del my_dict['Max']
print(my_dict)
my_set = {1, 1, 1, 1, 5, 2, 2, 3, 3}
print(my_set)
my_set.update([7, 9])
print(my_set)
my_set.discard(9)
print(my_set)
