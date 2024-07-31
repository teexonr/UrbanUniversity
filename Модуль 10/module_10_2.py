import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy, days = 100, 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            time.sleep(1)
            days += 1
            enemy -= self.power
            print(f'{self.name}, сражается {days} день(дня)..., осталось {enemy} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


knights = (('Sir Lancelot', 10), ('Sir Galahad', 20))
threads = []

for knight in knights:
    thread = Knight(*knight)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('Все битвы закончились!')
