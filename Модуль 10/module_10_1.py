from threading import Thread
from datetime import datetime
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w'):
        pass
    for n_word in range(word_count):
        print(f'Какое-то слово №{n_word}', file=open(file_name, 'a', encoding='utf-8'))
        sleep(0.1)
    print('Завершилась запись в файл', file_name)


numbers = (10, 30, 200, 100)
start_func = datetime.now()
for i, e in enumerate(numbers, start=1):
    write_words(e, f'example{i}.txt')
print('Работа функций:', datetime.now() - start_func)

threads = [Thread(target=write_words, args=(e, f'example{i}.txt'))
           for i, e in enumerate(numbers, start=5)]
start_thread = datetime.now()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print('Работа потоков:', datetime.now() - start_thread)
