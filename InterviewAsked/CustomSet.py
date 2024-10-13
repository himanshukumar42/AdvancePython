class CustomSet:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_keys = self.keys
        self.capacity *= 2
        self.keys = [None] * self.capacity

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.keys[i] = old_keys[i]

    def add(self, item):
        if self.size >= self.capacity:
            self._resize()

        index = self._hash(item)
        initial_index = index
        while self.keys[index] is not None:
            if self.keys[index] == item:
                return
            index = (index + 1) % self.capacity

            if index == initial_index:
                raise RuntimeError("Hashtable is full")

        self.keys[index] = item
        self.size += 1

    def remove(self, item):
        index = self._hash(item)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == item:
                self.keys[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity

            if index == initial_index:
                break

        raise ValueError(f"item {item} not in the set")

    def __len__(self):
        return self.size

    def __contains__(self, item):
        index = self._hash(item)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == item:
                return True

            index = (index + 1) % self.capacity

            if index == initial_index:
                break
        return False

    def __repr__(self):
        st = "{"
        for k in self.keys:
            if k is not None:
                st = st + str(k) + ", "
        st = st[:-2] + "}"
        return st


def main() -> None:
    my_set = CustomSet()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    my_set.add(4)
    my_set.add(5)
    my_set.add(6)
    my_set.add(7)
    my_set.add(8)
    my_set.add(9)
    print(my_set)
    print(len(my_set))
    my_set.remove(7)
    print(my_set)
    print(len(my_set))
    print(3 in my_set)

if __name__ == '__main__':
    main()
