class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        with open(self.__file_name, 'a') as _:
            pass

    def get_products(self):
        with open(self.__file_name) as output_:
            return ''.join(x for x in output_)

    def add(self, *products):
        for product in products:
            ex_products = [x.split(', ')[0] for x in self.get_products().split('\n') if x]
            if product.name not in ex_products:
                print(product, file=open(self.__file_name, 'a'))
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
