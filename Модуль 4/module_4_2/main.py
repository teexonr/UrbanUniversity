def function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


function()
try:
    inner_function()
except:
    print('Не получается вызвать inner_function')
