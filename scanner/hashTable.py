from collections import deque


class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__items = [deque() for _ in range(size)]

    # do not confuse with internal __hash__
    def hash(self, key):
        key_hash = 0
        for char in key[0]:
            key_hash += ord(char) - ord('0')
        return key_hash % self.__size

    def contains(self, key):
        return key in self.__items[self.hash(key)]

    def get_position(self, key):
        list_position = self.hash(key)
        list_index = 0
        for item in self.__items[list_position]:
            if item != key:
                list_index += 1
            else:
                break
        return list_position, list_index

    def add(self, key):
        if self.contains(key):
            return self.get_position(key)
        self.__items[self.hash(key)].append(key)
        return self.get_position(key)

    def remove(self, key):
        self.__items[self.hash(key)].remove(key)

    def __str__(self):
        result = ""
        for i in range(self.__size):
            result += str(i) + " -> " + str(self.__items[i]) + "\n"
        return result
