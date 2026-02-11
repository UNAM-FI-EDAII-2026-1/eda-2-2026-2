import unittest
from src.main import bubble_sort, merge_sort, quick_sort, heap_sort, counting_sort, radix_sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(bubble_sort([3, 0, 2, 5, -1, 4, 1]), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(merge_sort([3, 0, 2, 5, -1, 4, 1]), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(quick_sort([3, 0, 2, 5, -1, 4, 1]), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])
        # Test con duplicados
        self.assertEqual(quick_sort([4, 4, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 4])

    def test_heap_sort(self):
        self.assertEqual(heap_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(heap_sort([3, 0, 2, 5, -1, 4, 1]), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([1]), [1])
        # Test con duplicados
        self.assertEqual(heap_sort([4, 4, 4, 3, 3, 2, 1]), [1, 2, 3, 3, 4, 4, 4])

    def test_counting_sort(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])
        self.assertEqual(counting_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(counting_sort([]), [])
        self.assertEqual(counting_sort([1]), [1])
        # Test con muchos duplicados
        self.assertEqual(counting_sort([1, 1, 1, 2, 2, 3, 1]), [1, 1, 1, 1, 2, 2, 3])
        # Test con números grandes
        self.assertEqual(counting_sort([100, 50, 75, 25]), [25, 50, 75, 100])

    def test_radix_sort(self):
        self.assertEqual(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]), [2, 24, 45, 66, 75, 90, 170, 802])
        self.assertEqual(radix_sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(radix_sort([]), [])
        self.assertEqual(radix_sort([1]), [1])
        # Test con números de diferente longitud
        self.assertEqual(radix_sort([1000, 1, 100, 10]), [1, 10, 100, 1000])
        # Test con duplicados
        self.assertEqual(radix_sort([111, 111, 222, 333, 222]), [111, 111, 222, 222, 333])

if __name__ == "__main__":
    unittest.main()
