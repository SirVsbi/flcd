from hashTable import HashTable


class SymbolTable:

    def __init__(self, size):
        self.__hash_table = HashTable(size)

    def __str(self):
        return str(self.__hash_table)

    def add(self, key):
        return self.__hash_table.add(key)

    def contains(self, key):
        return self.__hash_table.contains(key)

    def remove(self, key):
        return self.__hash_table.remove(key)

    def get_position(self, key):
        return self.__hash_table.get_position(key)

    def __str__(self):
        return str(self.__hash_table)
