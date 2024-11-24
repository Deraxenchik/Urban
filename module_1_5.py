immutable_var = 1, 2, 3, True, "Python"
#immutable_var[0] = 200 - Не получится, потому что это тип данных, в котором нельзя изменять значения
print(immutable_var)
mutable_list = [1, 2, 3, True, "Python"]
mutable_list[0] = 200
print(mutable_list)