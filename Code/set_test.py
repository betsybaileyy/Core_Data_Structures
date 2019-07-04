#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set([1, 2, 3])
        assert test_set.size == 3
        assert test_set.contains(3) == True
        assert test_set.contains(5) == False

    def test_contains(self):
        test_set = Set([1, 2, 3])
        assert test_set.contains(3) == True
        assert test_set.contains(5) == False
        assert test_set.contains(6) == False
        assert test_set.contains(7) == False
        assert test_set.contains(1) == True

    def test_add(self):
        test_set = Set()
        test_set.add(5)
        test_set.add(3)
        test_set.add(9)
        test_set.add(8)
        assert test_set.contains(3) == True
        assert test_set.contains(5) == True
        assert test_set.contains(11) == False
        assert test_set.contains(12) == False

    def test_remove(self):
        test_set = Set([1, 2, 3, 4, 5, 6, 7])
        test_set.remove(5)
        test_set.remove(3)
        assert test_set.contains(3) == False
        assert test_set.contains(5) == False
        assert test_set.contains(6) == True
        assert test_set.contains(4) == True

    def test_union(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,4,8])
        unions = test_set.union(other_set)
        assert unions.contains(1)
        assert unions.contains(2)
        assert unions.contains(3)
        assert unions.contains(4)
        assert unions.contains(5)
        assert unions.contains(8)

    def test_intersection(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,3,7])
        unions = test_set.intersection(other_set)
        assert unions.contains(1)
        assert unions.contains(2)
        assert unions.contains(3)

    def test_difference(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,3,7])
        unions = test_set.difference(other_set)
        assert unions.contains(4) == True
        assert unions.contains(5) == True
        assert unions.contains(9) == False

    def test_is_subset(self):
        test_set = Set([1,2,3,4,5])
        other_set = Set([1,2,3])
        next_set = Set([7,8])
        assert test_set.is_subset(other_set) == True
        assert other_set.is_subset(test_set) == False
        assert next_set.is_subset(test_set) == False




if __name__ == '__main__':
    unittest.main()
