from quicksort import *
import unittest
class TestQuickSort(unittest.TestCase):
    def test_sort_arry_1(self):
        self.assertEqual(QuickSort().sort_array([]), [])

    def test_sort_array_2(self):
        self.assertEqual(QuickSort().sort_array([1]), [1])

    def test_sort_array_3(self):
        self.assertEqual(QuickSort().sort_array([2,1]), [1,2])
        
    def test_sort_array_4(self):
        self.assertEqual(QuickSort().sort_array([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]),
                         [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10])
    
if __name__ == "__main__":
    unittest.main()
    

