my_dict = {'Dmitry':1987, 'Katya':1991, 'Vova':2014}
print(my_dict)
print('Existing value:', my_dict.get('Dmitry'))
print('Not existing value:', my_dict.get('Alex', 'отсутствует'))
my_dict.update({'Tonya':1964, 'Anna':1994})
a = my_dict.pop('Dmitry')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
#
my_set = {11, 'синий', 3.14, 11, 3.14, 'зелёный', 'синий'}
print('Set:', my_set)
my_set.update([21, 'красный'])
print('Modified set:', my_set)