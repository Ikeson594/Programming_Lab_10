# Mike Wilkinson
# Programming Lab 10
# Unit Testing

# importing unittest

import unittest

# List manipulator

class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self):
        if len(self.list) == 0:
            return None

        min = self.list[0]
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self):
        if len(self.list) == 0:
            return None

        max = self.list[0]
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value):
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        removed_count = 0
        for index in to_remove:
            self.list.pop(index - removed_count)
            removed_count += 1


# creating the tests
class testmin(unittest.TestCase):
    def test1(self):
        List = ListManipulator([4, 2, 3, 1, 9, 3, 1, 3])
        minimum = List.min()
        self.assertEqual(minimum, 1)

    def test2(self):
        List = ListManipulator([4, 2, 1, 9, 3])
        minimum = List.min()
        self.assertEqual(minimum, 1)


# calling the tests

unittest.main()