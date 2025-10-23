#!/usr/bin/env python3
"""
Simple test runner for insertion sort tests.

This script provides an easy way to run different types of tests
for the insertion sort implementation.
"""

import sys
import argparse
from test_insertion_sort import (
    TestInsertionSortDecreasing,
    TestInsertionSortDecreasingInplace,
    TestPerformance,
    TestEdgeCases,
    TestNegativeCases,
    TestHelperFunctions,
    run_performance_benchmark,
    run_stress_test
)
import unittest


def run_unit_tests(verbose=False):
    """Run all unit tests."""
    print("Running Unit Tests...")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestInsertionSortDecreasing,
        TestInsertionSortDecreasingInplace,
        TestPerformance,
        TestEdgeCases,
        TestNegativeCases,
        TestHelperFunctions
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def run_quick_tests():
    """Run a quick subset of essential tests."""
    print("Running Quick Tests...")
    print("=" * 50)
    
    # Essential test cases
    essential_tests = [
        'test_insertion_sort.TestInsertionSortDecreasing.test_basic_sorting',
        'test_insertion_sort.TestInsertionSortDecreasing.test_empty_array',
        'test_insertion_sort.TestInsertionSortDecreasing.test_single_element',
        'test_insertion_sort.TestInsertionSortDecreasingInplace.test_basic_sorting',
        'test_insertion_sort.TestInsertionSortDecreasing.test_negative_numbers',
        'test_insertion_sort.TestInsertionSortDecreasing.test_duplicate_elements',
    ]
    
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    
    for test_name in essential_tests:
        try:
            test = loader.loadTestsFromName(test_name)
            suite.addTest(test)
        except Exception as e:
            print(f"Warning: Could not load test {test_name}: {e}")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def run_negative_tests(verbose=False):
    """Run only negative test cases."""
    print("Running Negative Test Cases...")
    print("=" * 50)
    
    # Create test suite with only negative tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add only negative test classes
    negative_test_classes = [
        TestNegativeCases,
        TestHelperFunctions  # Includes negative tests for helper functions
    ]
    
    for test_class in negative_test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description='Test runner for insertion sort implementation')
    parser.add_argument('--quick', action='store_true', 
                       help='Run only essential tests')
    parser.add_argument('--unit-only', action='store_true',
                       help='Run only unit tests (no benchmarks)')
    parser.add_argument('--benchmark', action='store_true',
                       help='Run only performance benchmarks')
    parser.add_argument('--stress', action='store_true',
                       help='Run only stress tests')
    parser.add_argument('--negative', action='store_true',
                       help='Run only negative test cases')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    
    args = parser.parse_args()
    
    print("Insertion Sort Test Runner")
    print("=" * 50)
    
    success = True
    
    if args.quick:
        success = run_quick_tests()
    elif args.benchmark:
        print("Running Performance Benchmarks...")
        run_performance_benchmark()
    elif args.stress:
        print("Running Stress Tests...")
        run_stress_test()
    elif args.negative:
        print("Running Negative Test Cases...")
        success = run_negative_tests(args.verbose)
    elif args.unit_only:
        success = run_unit_tests(args.verbose)
    else:
        # Run everything
        success = run_unit_tests(args.verbose)
        
        if success:
            print("\n" + "=" * 50)
            run_performance_benchmark()
            
            print("\n" + "=" * 50)
            run_stress_test()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ All tests passed successfully!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
