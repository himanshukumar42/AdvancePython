class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = {}
        self.is_paid = False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.order_id}, {self.customer_name}, {self.items})"

    def __str__(self):
        all_items = ", ".join(self.items)
        return f"Order {self.order_id} for Customer {self.customer_name} with items {all_items}"

    def __len__(self):
        return sum(self.items.values())

    def __setitem__(self, item, quantity):
        if quantity > 0:
            self.items[item] = quantity
        elif item in self.items:
            del self.items[item]

    def __getitem__(self, item):
        if item in self.items:
            return self.items[item]

    def __delitem__(self, item):
        if item in self.items:
            del self.items[item]

    def __eq__(self, other):
        return sum(self.items.values()) == sum(other.items.values())

    def __lt__(self, other):
        return sum(self.items.values()) < sum(other.items.values())

    def __gt__(self, other):
        return sum(self.items.values()) > sum(other.items.values())

    def __le__(self, other):
        return sum(self.items.values()) <= sum(other.items.values())

    def __ge__(self, other):
        return sum(self.items.values()) >= sum(other.items.values())

    def __ne__(self, other):
        return sum(self.items.values()) != sum(other.items.values())

    def __contains__(self, item):
        return item in self.items

    def __hash__(self):
        return hash(self.order_id)

    def __iter__(self):
        return iter(self.items.items())

    def __next__(self):
        return next(self.__iter__())

    def __enter__(self):
        print(f"Starting checkout for order {self.order_id}...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.is_paid:
            print(f"Order {self.order_id} has been processed successfully.")
        else:
            print(f"Checkout for order {self.order_id} failed or cancelled.")

    def total_cost(self):
        return len(self) * 10

    def __call__(self, amount):
        total = self.total_cost()
        if self.is_paid:
            print(f"Payment of {amount} already made for Order {self.order_id}")
        elif amount >= total:
            self.is_paid = True
            print(f"Payment of {amount} accepted. Order {self.order_id} has been processed successfully.")
        else:
            print(f"Insufficient payment. {amount} is less than the order values. payment failed")

    def __mul__(self, val: int):
        new_order = Order(self.order_id, self.customer_name)
        new_order.items = {key: value * val for key, value in self.items.items()}
        return new_order

    def __rmul__(self, val: int):
        return self.__mul__(val)

    def __del__(self):
        print(f"{self.__class__.__name__}({self.order_id}, {self.customer_name}, {self.items}) object is being deleted")


def order_generator(order: Order):
    for o in order:
        yield o


def main() -> None:
    order = Order("101", "Alice")
    order["Laptop"] = 1
    order["Mouse"] = 2
    order["Phone"] = 1
    order["Headphones"] = 1

    print(order["Laptop"])
    print(order["Mouse"])

    # order(400)
    # with order:
    #     order(400)
    # with Order(103, "Charlie") as order2:
    #     order2["Tablet"] = 2
    #     order2(100)

    # print("Mouse" in order)
    multiplied_order = 2 * order
    print(multiplied_order)


if __name__ == '__main__':
    main()
