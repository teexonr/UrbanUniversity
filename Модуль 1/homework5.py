# Неизменяемые и изменяемые объекты. Кортежи

immutable_var = (1, True, '')
print('Immutable tuple:', immutable_var)
try:
    immutable_var[0] = 0
except:
    print('Ошибка! Кортеж – неизменяемый тип данных')
    
mutable_var = [1, True, '']
print('Mutable list:', [not x for x in mutable_var])
