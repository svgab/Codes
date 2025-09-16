import unittest
import first

class TestMySolution(unittest.TestCase):

    def test_same_lst_elems(self):
        self.assertEqual(first.Solution().two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(first.Solution().two_sum([3, 3, 3, 3], 6), (0, 1))
        self.assertEqual(first.Solution().two_sum([16, 2, 15, 89], 105), (0, 3))

if __name__ == '__main__':
    unittest.main()