import unittest
import my_sorts as local_sorts
class LearnSorts(unittest.TestCase):
    def test_bubble_sort(self):
        # result = local_sorts.bubble_sort()
        result = local_sorts.bubble_sort([3,1,-3,8,-2,1])
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()