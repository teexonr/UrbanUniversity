import queue
import time
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(Thread):
    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.number} покушал за столиком и ушёл.')
        self.table.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customers = []

    def customer_arrival(self):
        for people in range(1, 21):
            time.sleep(1)
            print(f'Посетитель номер {people} прибыл.')
            self.serve_customer(people)

    def serve_customer(self, people):
        for table in self.tables:
            if not table.is_busy:
                self.queue.put(people)
                customer = Customer(self.queue.get(), table)
                table.is_busy = True
                print(f'Посетитель номер {customer.number} сел за стол {table.number}.')
                customer.start()
                self.customers.append(customer)
                break
        else:
            self.queue.put(people)
            print(f'Посетитель номер {people} ожидает свободный стол.')


# Создаем столики в кафе
tables_list = [Table(1), Table(2), Table(3)]

# Инициализируем кафе
cafe = Cafe(tables_list)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

for customer_ in cafe.customers:
    customer_.join()