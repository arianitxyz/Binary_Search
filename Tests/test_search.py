import unittest
from binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):

    def setUp(self) -> None:
        self.binary = BinarySearch()
        self.binary.low = 1
        self.binary.high = 100

    def test_search_9(self):
        self.binary.answer = 9
        self.assertEqual(self.binary.search(), 5)

    def test_search_0(self):
        self.binary.answer = 0
        self.assertEqual(self.binary.search(), 0)

    def test_search_30(self):
        self.binary.answer = 30
        self.assertEqual(self.binary.search(), 7)

    def test_search_20(self):
        self.binary.answer = 20
        self.assertEqual(self.binary.search(), 7)


if __name__ == '__main__':
    unittest.main()