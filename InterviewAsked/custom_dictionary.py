class CustomDict:
    def __init__(self, capacity=8):
        self.capacity = capacity  # size of hash table
        self.size = 0  # Number of key-value pairs
        self.keys = [None] * capacity  # Array to store keys
        self.values = [None] * capacity  # Array to store values

    def _hash(self, key):
        """Generate a hash for the key"""
        return hash(key) % self.capacity

    def _resize(self):
        """Resize the hash table when it reaches capacity"""
        old_keys = self.keys
        old_values = self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0  # Reset size and reinsert elements

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self[old_keys[i]] = old_values[i]

    def __setitem__(self, key, value):
        if self.size >= self.capacity // 2:
            self._resize()  # Resize the load factor exceeds 0.5

        index = self._hash(key)
        initial_index = index  # For detection of full table condition
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.capacity  # Linear Probing

            if index == initial_index:  # The table is full, resize needed
                raise RuntimeError("Hashtable is full")

        # Insert new key-value pair
        self.keys[index] = key
        self.values[index] = value
        self.size += 1

    def __getitem__(self, key):
        """ Retrieve a value by its key. """
        index = self._hash(key)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity  # Linear Probing

            if index == initial_index:
                break

        raise KeyError(f"Key '{key}' not found")

    def __delitem__(self, key):
        index = self._hash(key)
        initial_index = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys = None
                self.values = None
                self.size -= 1
                return
            index = (index + 1) % self.capacity

            if index == initial_index:
                break
        raise KeyError(f"Key '{key}' not found")

    def __repr__(self):
        """ Represents the dictionary of a string """
        return "{ " + ", ".join(
            f"'{self.keys[i]}':'{self.values[i]}'" for i in range(self.capacity) if self.keys[i] is not None
        ) + " }"


def main() -> None:
    my_dict = CustomDict()
    my_dict["name"] = "Himanshu Kumar"
    print(hash("himanshu") % 8)
    my_dict["age"] = 26
    my_dict["company"] = "Cloud"
    print(my_dict)
    hdl = {"hello": "arun"}
    print(hdl)


if __name__ == '__main__':
    main()
