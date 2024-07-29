def custom_write(file_name: str, strings: list) -> dict:
    file_dict = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for number, string in enumerate(strings, start=1):
            file_dict[(number, file.tell())] = string
            print(string, file=file)
    return file_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
