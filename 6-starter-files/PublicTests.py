import unittest
from solution import evalRPN

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(3, evalRPN(["1", "2", "+"]))

    def test2(self):
        self.assertEqual(-2, evalRPN(["5", "7", "-"]))

    def test3(self):
        self.assertEqual(23, evalRPN(["3", "4", "5", "*", "+"]))

    def test4(self):
        self.assertEqual(-33, evalRPN(["4", "7", "2", "/", "+", "8", "5", "*", "-"]))

if __name__ == "__main__":
    unittest.main()
