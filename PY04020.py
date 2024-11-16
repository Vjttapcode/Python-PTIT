class Product:
    def __init__(self, id, name, quantity, price, discount):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.total = self.price * self.quantity - self.discount

    def __lt__(self, other):
        return self.total > other.total

    def __str__(self):
        return f"{self.id} {self.name} {self.quantity} {self.price} {self.discount} {self.total}"

n = int(input())
list_products = []
for i in range(n):
    id = input()
    name = input()
    quantity = int(input())
    price = int(input())
    discount = int(input())
    product = Product(id, name, quantity, price, discount)
    list_products.append(product)

list_products.sort()
for product in list_products:
    print(product)