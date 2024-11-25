my_dict = {'Имя': 'Artem', 'Год рождения': 2006}
print(my_dict)
print(my_dict['Имя'])
print(my_dict.get('Номер телефона'))
my_dict.update({'Текущий год': 2024, 'Платформа обучения': 'Urban'})
a = my_dict.pop('Текущий год')
print(a)
print(my_dict)

my_set = {1, 1, 2, 2, 3, 3, 'String', 'String', 1, 2, 3}
print(my_set)
my_set.update('zxc')
my_set.remove(1)
print(my_set)