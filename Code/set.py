
from hashtable import HashTable

# set is a data structure of unordered and unique elements
class Set(object):
    def __init__(self, elements=None):
        """initialize a new empty set structure, and add each element if a sequence is given"""
        self.size = 0
        # map is just a dictionary with Key Value Pairs
        self.map = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)

    def add(self, element):
        """add element to this set, if not present already"""
        if not self.contains(element):
            self.size += 1
            self.map.set(element, None)

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        self.map.delete(element)
        self.size -= 1


    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        return self.map.contains(element)


    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        new_set = Set()
        for element in self.map.keys():
            new_set.add(element)

        for element in other_set.map.keys():
            if not new_set.contains(element):
                new_set.add(element)

        return new_set


    def intersection(self, other_set):
        new_set = Set()
        for element in other_set.map.keys():
            if self.contains(element):
                new_set.add(element)
        return new_set


    def difference(self, other_set):
        new_set = Set()
        for element in self.map.keys():
            if not other_set.contains(element):
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        for element in other_set.map.keys():
            if not self.contains(element):
                return False
        return True
