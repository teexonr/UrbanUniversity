from threading import Lock


class BankAccount:
    def __init__(self):
        self.__balance = 1000
        self._lock = Lock()

    def deposit(self, amount):
        with self._lock:
            self.__balance += amount
            print(f'Deposited {amount}, new balance is {self.__balance}')

    def withdraw(self, amount):
        with self._lock:
            self.__balance -= amount
            print(f'Withdrew {amount}, new balance is {self.__balance}')


def introspection_info(obj):
    return {
        'type': type(obj),
        'attributes': [a for a in dir(obj) if not callable(a)],
        'methods': [a for a in dir(obj) if callable(a)],
        'module': __name__
    }


info = introspection_info(BankAccount())
print(*info.items(), sep='\n')
