
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        else:
            self.head = Node(value)

    def contains(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def delete(self, value):
        if (self.head is None):
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next is not None:
            if node.value == value:
                break
            node = node.next

        if node.next is not None:
            node.next = node.next.next

    def __str__(self):
        text = ""
        node = self.head

        while node:
            text += str(node.value)
            if node.next:
                text += " -> "
            node = node.next

        return text


class HashTable:
    def __init__(self, size):
        self.size = size

    def put(self):
        raise NotImplementedError

    def hash(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def contains(self):
        raise NotImplementedError

    def get_index(self):
        raise NotImplementedError

    def display(self):
        for index, item in enumerate(self.table):
            print(f"Index: {index} - Value: {item}")


class HashTableOpenHashing(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.table = [LinkedList() for i in range(self.size)]

    def put(self, key):
        if self.contains(key):
            print("Cannot add a duplicate.")
        else:
            index = self.hash(key)
            self.table[index].insert(key)

    def hash(self, key):
        return key % self.size

    def delete(self, key):
        index = self.hash(key)
        self.table[index].delete(key)

    def contains(self, key):
        return self.get_index != -1

    def get_index(self, key):
        for index, linked_list in enumerate(self.table):
            if linked_list.contains(key):
                return index
        return -1


class HashTableOpenAddressing(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.table = [None] * self.size

    def put(self, key):
        if self.contains(key):
            print("Cannot add a duplicate.")
        elif None not in self.table:
            print("Cannot add anymore. Table is full.")
        else:
            index = self.hash(key)
            self.table[index] = key

    def delete(self, key):
        self.table.remove(key)

    def contains(self, key):
        return key in self.table

    def get_index(self, key):
        for index, item in enumerate(self.table):
            if key == item:
                return index
        return -1


class HashTableLinearProbing(HashTableOpenAddressing):
    def hash(self, key):
        index = key % self.size

        if self.table[index] is None:
            return index
        else:
            while self.table[index] is not None:
                index = (index + 1) % self.size
            return index


class HashTableQuadraticProbing(HashTableOpenAddressing):
    def hash(self, key):
        index = key % self.size

        if self.table[index] is None:
            return index
        else:
            i = 0
            while self.table[(index + (i * i)) % self.size] is not None:
                i += 1
            return (index + (i * i)) % self.size


class HashTableDoubleHashing(HashTableOpenAddressing):
    def hash(self, key):
        prime = 2
        hash_one = key % self.size
        hash_two = prime - key % prime

        if self.table[hash_one] is None:
            return hash_one
        else:
            i = 0
            while self.table[hash_one + i * hash_two] is not None:
                i += 1
            return hash_one + i * hash_two


if __name__ == "__main__":
    pass
