from abc import ABC, abstractmethod


class ProductComponent(ABC):
    @abstractmethod
    def show_details(self, indent: int = 0):
        pass


class Product(ProductComponent):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def show_details(self, indent: int = 0):
        print(" "*indent + f"Product: {self._name} - ${self._price}")


class ProductCategory(ProductComponent):
    def __init__(self, name):
        self._name = name
        self._categories = []

    def add(self, category: ProductComponent):
        self._categories.append(category)

    def remove(self, category: ProductComponent):
        self._categories.remove(category)

    def show_details(self, indent: int = 0):
        print(" "*indent + f"Category: {self._name}")
        for category in self._categories:
            category.show_details(indent+4)


def main() -> None:
    all_category = ProductCategory("All")
    electronics = ProductCategory("Electronics")
    apparel = ProductCategory("Apparel")
    books = ProductCategory("Books")

    laptop = ProductCategory("Laptops")
    phones = ProductCategory("Phones")

    mens_clothes = ProductCategory("Mens")
    tshirt = ProductCategory("tshirt")
    shirt = ProductCategory("Shirt")
    jeans = ProductCategory("Jeans")
    woman_clothes = ProductCategory("Women")

    macbook = Product("Macbook Pro", 1500)
    iphone = Product("Iphone 14 Pro Max", 1000)

    laptop.add(macbook)
    phones.add(iphone)

    apparel.add(mens_clothes)
    apparel.add(woman_clothes)

    mens_clothes.add(tshirt)
    mens_clothes.add(shirt)
    mens_clothes.add(jeans)

    electronics.add(laptop)
    electronics.add(phones)

    all_category.add(electronics)
    all_category.add(apparel)
    all_category.add(books)
    all_category.show_details()


if __name__ == '__main__':
    main()
