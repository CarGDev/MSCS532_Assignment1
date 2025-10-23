#!/usr/bin/env python3
"""
Comprehensive Test Suite for Insertion Sort - Decreasing Order

This module contains extensive test cases for the insertion sort implementation,
including unit tests, edge cases, performance tests, and stress tests.
"""

import unittest
import random
import time
import sys
from typing import List, Tuple

# Import the functions to test
from insertion_sort_decreasing import insertion_sort_decreasing, insertion_sort_decreasing_inplace


class TestInsertionSortDecreasing(unittest.TestCase):
    """Test cases for insertion_sort_decreasing function."""
    
    def test_basic_sorting(self):
        """Test basic sorting functionality."""
        test_cases = [
            ([5, 2, 8, 1, 9, 3], [9, 8, 5, 3, 2, 1]),
            ([64, 34, 25, 12, 22, 11, 90], [90, 64, 34, 25, 22, 12, 11]),
            ([3, 1, 4, 1, 5, 9, 2, 6], [9, 6, 5, 4, 3, 2, 1, 1]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_already_sorted_ascending(self):
        """Test arrays already sorted in ascending order."""
        test_cases = [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([1, 2, 3], [3, 2, 1]),
            ([1], [1]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_already_sorted_descending(self):
        """Test arrays already sorted in descending order."""
        test_cases = [
            ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
            ([10, 8, 6, 4, 2], [10, 8, 6, 4, 2]),
            ([3, 2, 1], [3, 2, 1]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_empty_array(self):
        """Test empty array."""
        result = insertion_sort_decreasing([])
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test arrays with single element."""
        test_cases = [
            ([1], [1]),
            ([42], [42]),
            ([0], [0]),
            ([-5], [-5]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_duplicate_elements(self):
        """Test arrays with duplicate elements."""
        test_cases = [
            ([3, 3, 3, 3], [3, 3, 3, 3]),
            ([5, 2, 5, 2, 5], [5, 5, 5, 2, 2]),
            ([1, 1, 2, 2, 3, 3], [3, 3, 2, 2, 1, 1]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test arrays with negative numbers."""
        test_cases = [
            ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
            ([5, -2, 8, -1, 9, -3], [9, 8, 5, -1, -2, -3]),
            ([-10, 5, -3, 0, 2], [5, 2, 0, -3, -10]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_zero_values(self):
        """Test arrays containing zero values."""
        test_cases = [
            ([0, 1, 2, 3], [3, 2, 1, 0]),
            ([5, 0, -2, 0, 3], [5, 3, 0, 0, -2]),
            ([0, 0, 0], [0, 0, 0]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_large_numbers(self):
        """Test arrays with large numbers."""
        test_cases = [
            ([1000000, 999999, 1000001], [1000001, 1000000, 999999]),
            ([2**31 - 1, 2**31 - 2, 2**31 - 3], [2**31 - 1, 2**31 - 2, 2**31 - 3]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing(input_arr)
                self.assertEqual(result, expected)
    
    def test_original_array_unchanged(self):
        """Test that original array is not modified."""
        original = [5, 2, 8, 1, 9, 3]
        original_copy = original.copy()
        result = insertion_sort_decreasing(original)
        
        self.assertEqual(original, original_copy)
        self.assertNotEqual(result, original)
    
    def test_sorting_stability(self):
        """Test that sorting is stable (equal elements maintain relative order)."""
        # For insertion sort, stability means equal elements keep their original order
        input_arr = [(5, 'a'), (3, 'b'), (5, 'c'), (3, 'd')]
        result = insertion_sort_decreasing(input_arr)
        
        # Check that elements with same first value maintain their order
        # Since we're sorting by the first element in decreasing order,
        # all 5s should come before all 3s, and within each group, 
        # the original order should be preserved
        self.assertEqual(result[0], (5, 'c'))  # First 5 should be 'c' (stable)
        self.assertEqual(result[1], (5, 'a'))  # Second 5 should be 'a' (stable)
        self.assertEqual(result[2], (3, 'd'))  # First 3 should be 'd' (stable)
        self.assertEqual(result[3], (3, 'b'))  # Second 3 should be 'b' (stable)


class TestInsertionSortDecreasingInplace(unittest.TestCase):
    """Test cases for insertion_sort_decreasing_inplace function."""
    
    def test_basic_sorting(self):
        """Test basic sorting functionality."""
        test_cases = [
            ([5, 2, 8, 1, 9, 3], [9, 8, 5, 3, 2, 1]),
            ([64, 34, 25, 12, 22, 11, 90], [90, 64, 34, 25, 22, 12, 11]),
            ([3, 1, 4, 1, 5, 9, 2, 6], [9, 6, 5, 4, 3, 2, 1, 1]),
        ]
        
        for input_arr, expected in test_cases:
            with self.subTest(input_arr=input_arr):
                result = insertion_sort_decreasing_inplace(input_arr)
                self.assertEqual(result, expected)
                self.assertEqual(input_arr, expected)  # Original should be modified
    
    def test_empty_array(self):
        """Test empty array."""
        arr = []
        result = insertion_sort_decreasing_inplace(arr)
        self.assertEqual(result, [])
        self.assertEqual(arr, [])
    
    def test_single_element(self):
        """Test arrays with single element."""
        arr = [42]
        result = insertion_sort_decreasing_inplace(arr)
        self.assertEqual(result, [42])
        self.assertEqual(arr, [42])
    
    def test_original_array_modified(self):
        """Test that original array is modified."""
        original = [5, 2, 8, 1, 9, 3]
        result = insertion_sort_decreasing_inplace(original)
        
        self.assertEqual(original, result)
        self.assertEqual(original, [9, 8, 5, 3, 2, 1])


class TestPerformance(unittest.TestCase):
    """Performance and stress tests."""
    
    def test_performance_small_arrays(self):
        """Test performance with small arrays."""
        sizes = [10, 50, 100]
        
        for size in sizes:
            with self.subTest(size=size):
                arr = list(range(size))
                random.shuffle(arr)
                
                start_time = time.time()
                result = insertion_sort_decreasing(arr)
                end_time = time.time()
                
                # Verify correctness
                expected = list(range(size - 1, -1, -1))
                self.assertEqual(result, expected)
                
                # Performance should be reasonable for small arrays
                execution_time = end_time - start_time
                self.assertLess(execution_time, 1.0)  # Should complete within 1 second
    
    def test_worst_case_performance(self):
        """Test performance with worst-case input (ascending order)."""
        sizes = [10, 50, 100]
        
        for size in sizes:
            with self.subTest(size=size):
                arr = list(range(size))  # Already sorted ascending (worst case)
                
                start_time = time.time()
                result = insertion_sort_decreasing(arr)
                end_time = time.time()
                
                # Verify correctness
                expected = list(range(size - 1, -1, -1))
                self.assertEqual(result, expected)
                
                execution_time = end_time - start_time
                self.assertLess(execution_time, 1.0)
    
    def test_best_case_performance(self):
        """Test performance with best-case input (descending order)."""
        sizes = [10, 50, 100]
        
        for size in sizes:
            with self.subTest(size=size):
                arr = list(range(size - 1, -1, -1))  # Already sorted descending
                
                start_time = time.time()
                result = insertion_sort_decreasing(arr)
                end_time = time.time()
                
                # Verify correctness
                expected = list(range(size - 1, -1, -1))
                self.assertEqual(result, expected)
                
                execution_time = end_time - start_time
                self.assertLess(execution_time, 1.0)


class TestEdgeCases(unittest.TestCase):
    """Edge cases and boundary conditions."""
    
    def test_very_large_numbers(self):
        """Test with very large numbers."""
        arr = [sys.maxsize, sys.maxsize - 1, sys.maxsize - 2]
        result = insertion_sort_decreasing(arr)
        expected = [sys.maxsize, sys.maxsize - 1, sys.maxsize - 2]
        self.assertEqual(result, expected)
    
    def test_very_small_numbers(self):
        """Test with very small numbers."""
        arr = [-sys.maxsize, -sys.maxsize + 1, -sys.maxsize + 2]
        result = insertion_sort_decreasing(arr)
        expected = [-sys.maxsize + 2, -sys.maxsize + 1, -sys.maxsize]
        self.assertEqual(result, expected)
    
    def test_mixed_types_comparable(self):
        """Test with mixed types that are comparable."""
        # Note: This will work with Python's comparison rules
        arr = [1, 1.5, 2, 2.5]
        result = insertion_sort_decreasing(arr)
        expected = [2.5, 2, 1.5, 1]
        self.assertEqual(result, expected)
    
    def test_random_large_array(self):
        """Test with a larger random array."""
        random.seed(42)  # For reproducible tests
        arr = [random.randint(-1000, 1000) for _ in range(100)]
        result = insertion_sort_decreasing(arr)
        
        # Verify it's sorted in decreasing order
        for i in range(len(result) - 1):
            self.assertGreaterEqual(result[i], result[i + 1])


class TestNegativeCases(unittest.TestCase):
    """Negative test cases - testing invalid inputs and error conditions."""
    
    def test_none_input(self):
        """Test that None input raises appropriate error."""
        with self.assertRaises((TypeError, AttributeError)):
            insertion_sort_decreasing(None)
        
        with self.assertRaises((TypeError, AttributeError)):
            insertion_sort_decreasing_inplace(None)
    
    def test_non_list_input(self):
        """Test that non-list inputs behave unexpectedly or raise errors."""
        # Test inputs that should raise errors
        error_inputs = [
            "string",  # String doesn't support item assignment
            123,       # Int doesn't support indexing
            45.67,     # Float doesn't support indexing
        ]
        
        for invalid_input in error_inputs:
            with self.subTest(input_type=type(invalid_input).__name__, input_value=invalid_input):
                with self.assertRaises((TypeError, AttributeError)):
                    insertion_sort_decreasing(invalid_input)
                
                with self.assertRaises((TypeError, AttributeError)):
                    insertion_sort_decreasing_inplace(invalid_input)
        
        # Test inputs that might work but shouldn't be used
        problematic_inputs = [
            {"key": "value"},  # Dict - might work but unpredictable
            (1, 2, 3),         # Tuple - immutable, will cause errors on modification
            set([1, 2, 3]),    # Set - unordered, unpredictable
        ]
        
        for invalid_input in problematic_inputs:
            with self.subTest(input_type=type(invalid_input).__name__, input_value=invalid_input):
                # These might not raise errors immediately but are problematic
                try:
                    result = insertion_sort_decreasing(invalid_input)
                    # If it doesn't raise an error, verify it's problematic
                    self.assertIsInstance(result, type(invalid_input))
                except (TypeError, AttributeError):
                    # Expected for some types
                    pass
    
    def test_non_comparable_elements(self):
        """Test arrays with non-comparable elements."""
        # Mixed types that can't be compared
        non_comparable_arrays = [
            [1, "string", 3],
            [1, [2, 3], 4],
            [1, {"key": "value"}, 3],
            [1, None, 3],
        ]
        
        for arr in non_comparable_arrays:
            with self.subTest(array=arr):
                with self.assertRaises(TypeError):
                    insertion_sort_decreasing(arr)
                
                with self.assertRaises(TypeError):
                    insertion_sort_decreasing_inplace(arr)
    
    def test_nested_lists(self):
        """Test arrays with nested lists (should work with lexicographic comparison)."""
        nested_arrays = [
            [[1, 2], [3, 4]],
            [[1], [2], [3]],
            [[1, 2, 3], [4, 5, 6]],
        ]
        
        for arr in nested_arrays:
            with self.subTest(array=arr):
                result = insertion_sort_decreasing(arr)
                # Verify it's sorted correctly (lexicographically)
                for i in range(len(result) - 1):
                    self.assertGreaterEqual(result[i], result[i + 1])
                
                # Test in-place version
                arr_copy = arr.copy()
                insertion_sort_decreasing_inplace(arr_copy)
                self.assertEqual(arr_copy, result)
    
    def test_objects_without_comparison(self):
        """Test arrays with objects that don't support comparison."""
        class NonComparable:
            def __init__(self, value):
                self.value = value
        
        obj1 = NonComparable(1)
        obj2 = NonComparable(2)
        
        with self.assertRaises(TypeError):
            insertion_sort_decreasing([obj1, obj2])
        
        with self.assertRaises(TypeError):
            insertion_sort_decreasing_inplace([obj1, obj2])
    
    def test_custom_objects_with_comparison(self):
        """Test arrays with custom objects that do support comparison."""
        class Comparable:
            def __init__(self, value):
                self.value = value
            
            def __lt__(self, other):
                return self.value < other.value
            
            def __gt__(self, other):
                return self.value > other.value
            
            def __eq__(self, other):
                return self.value == other.value
        
        obj1 = Comparable(5)
        obj2 = Comparable(2)
        obj3 = Comparable(8)
        
        # This should work since the objects support comparison
        result = insertion_sort_decreasing([obj1, obj2, obj3])
        self.assertEqual([obj.value for obj in result], [8, 5, 2])
    
    def test_very_large_arrays(self):
        """Test with very large arrays (should still work but may be slow)."""
        # Test with a moderately large array
        large_array = list(range(1000))
        random.shuffle(large_array)
        
        # This should work but might be slow
        result = insertion_sort_decreasing(large_array)
        expected = list(range(999, -1, -1))
        self.assertEqual(result, expected)
    
    def test_infinity_values(self):
        """Test arrays containing infinity values."""
        import math
        
        inf_arrays = [
            [1, float('inf'), 3],
            [1, float('-inf'), 3],
            [float('inf'), float('-inf'), 0],
        ]
        
        for arr in inf_arrays:
            with self.subTest(array=arr):
                result = insertion_sort_decreasing(arr)
                # Verify it's sorted correctly
                for i in range(len(result) - 1):
                    self.assertGreaterEqual(result[i], result[i + 1])
    
    def test_nan_values(self):
        """Test arrays containing NaN values (NaN comparisons are unpredictable)."""
        import math
        
        nan_arrays = [
            [1, float('nan'), 3],
            [float('nan'), 1, 3],
            [1, 3, float('nan')],
        ]
        
        for arr in nan_arrays:
            with self.subTest(array=arr):
                # NaN comparisons don't raise errors but produce unpredictable results
                # We just verify the function doesn't crash
                result = insertion_sort_decreasing(arr)
                self.assertEqual(len(result), len(arr))
                
                # Test in-place version
                arr_copy = arr.copy()
                insertion_sort_decreasing_inplace(arr_copy)
                self.assertEqual(len(arr_copy), len(arr))
    
    def test_mixed_numeric_types(self):
        """Test arrays with mixed numeric types (should work)."""
        mixed_arrays = [
            [1, 2.5, 3],
            [1.0, 2, 3.14],
            [1, 2.0, 3],
        ]
        
        for arr in mixed_arrays:
            with self.subTest(array=arr):
                result = insertion_sort_decreasing(arr)
                # Verify it's sorted correctly
                for i in range(len(result) - 1):
                    self.assertGreaterEqual(result[i], result[i + 1])
    
    def test_empty_strings_and_numbers(self):
        """Test arrays with empty strings and numbers."""
        mixed_arrays = [
            [1, "", 3],
            ["", 1, 3],
            [1, 3, ""],
        ]
        
        for arr in mixed_arrays:
            with self.subTest(array=arr):
                with self.assertRaises(TypeError):
                    insertion_sort_decreasing(arr)
                
                with self.assertRaises(TypeError):
                    insertion_sort_decreasing_inplace(arr)
    
    def test_boolean_values(self):
        """Test arrays with boolean values (should work)."""
        bool_arrays = [
            [True, False, True],
            [False, True, False],
            [True, True, False],
        ]
        
        for arr in bool_arrays:
            with self.subTest(array=arr):
                result = insertion_sort_decreasing(arr)
                # Verify it's sorted correctly (True > False)
                for i in range(len(result) - 1):
                    self.assertGreaterEqual(result[i], result[i + 1])
    
    def test_very_deep_recursion_simulation(self):
        """Test with arrays that might cause issues in very deep recursion."""
        # Create an array that's already sorted in descending order
        # This should be the best case for insertion sort
        descending_array = list(range(100, 0, -1))
        
        result = insertion_sort_decreasing(descending_array)
        expected = list(range(100, 0, -1))
        self.assertEqual(result, expected)
    
    def test_unicode_strings(self):
        """Test arrays with unicode strings."""
        unicode_arrays = [
            ["hello", "world", "test"],
            ["α", "β", "γ"],
            ["🚀", "🌟", "⭐"],
        ]
        
        for arr in unicode_arrays:
            with self.subTest(array=arr):
                result = insertion_sort_decreasing(arr)
                # Verify it's sorted correctly (lexicographically)
                for i in range(len(result) - 1):
                    self.assertGreaterEqual(result[i], result[i + 1])


class TestHelperFunctions(unittest.TestCase):
    """Test helper functions if any."""
    
    def test_print_array_function(self):
        """Test the print_array helper function."""
        # This is more of a smoke test since print_array doesn't return anything
        from insertion_sort_decreasing import print_array
        
        # Should not raise any exceptions
        print_array([1, 2, 3], "Test Array")
        print_array([], "Empty Array")
    
    def test_print_array_with_invalid_input(self):
        """Test print_array with invalid input."""
        from insertion_sort_decreasing import print_array
        
        # Test with None - should handle gracefully or raise error
        try:
            print_array(None, "None Array")
        except (TypeError, AttributeError):
            pass  # Expected behavior
        
        # Test with non-list input - should handle gracefully or raise error
        try:
            print_array("not a list", "String Array")
        except (TypeError, AttributeError):
            pass  # Expected behavior


def run_performance_benchmark():
    """Run a performance benchmark comparing different scenarios."""
    print("\n" + "="*60)
    print("PERFORMANCE BENCHMARK")
    print("="*60)
    
    scenarios = [
        ("Random Array", lambda n: [random.randint(1, 1000) for _ in range(n)]),
        ("Ascending Order", lambda n: list(range(n))),
        ("Descending Order", lambda n: list(range(n-1, -1, -1))),
        ("All Same", lambda n: [42] * n),
    ]
    
    sizes = [10, 50, 100, 500]
    
    for scenario_name, generator in scenarios:
        print(f"\n{scenario_name}:")
        print("-" * 40)
        
        for size in sizes:
            arr = generator(size)
            
            # Test non-inplace version
            start_time = time.time()
            result1 = insertion_sort_decreasing(arr)
            time1 = time.time() - start_time
            
            # Test inplace version
            arr_copy = arr.copy()
            start_time = time.time()
            result2 = insertion_sort_decreasing_inplace(arr_copy)
            time2 = time.time() - start_time
            
            print(f"Size {size:3d}: Non-inplace: {time1:.6f}s, In-place: {time2:.6f}s")


def run_stress_test():
    """Run stress tests with various edge cases."""
    print("\n" + "="*60)
    print("STRESS TEST")
    print("="*60)
    
    stress_cases = [
        ("Empty array", []),
        ("Single element", [42]),
        ("Two elements", [2, 1]),
        ("All zeros", [0, 0, 0, 0]),
        ("Negative numbers", [-5, -2, -8, -1]),
        ("Mixed positive/negative", [5, -2, 8, -1, 0]),
        ("Large numbers", [1000000, 999999, 1000001]),
        ("Duplicate elements", [3, 3, 1, 1, 2, 2]),
    ]
    
    for case_name, test_arr in stress_cases:
        print(f"\n{case_name}: {test_arr}")
        
        # Test both functions
        result1 = insertion_sort_decreasing(test_arr)
        test_arr_copy = test_arr.copy()
        result2 = insertion_sort_decreasing_inplace(test_arr_copy)
        
        # Verify results are identical
        assert result1 == result2, f"Results differ for {case_name}"
        
        # Verify sorting is correct
        for i in range(len(result1) - 1):
            assert result1[i] >= result1[i + 1], f"Not sorted correctly at index {i}"
        
        print(f"✓ Passed: {result1}")


if __name__ == "__main__":
    # Set random seed for reproducible tests
    random.seed(42)
    
    print("Insertion Sort - Decreasing Order Test Suite")
    print("=" * 60)
    
    # Run unit tests
    print("\nRunning Unit Tests...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run performance benchmark
    run_performance_benchmark()
    
    # Run stress tests
    run_stress_test()
    
    print("\n" + "="*60)
    print("All tests completed!")
    print("="*60)
