from faker import Faker

fake = Faker("Ru-ru")


class Product:
    def __init__(self, product=None):
        self.product = product

    @staticmethod
    def random():
        product = fake.word()
        return Product(product=product)
