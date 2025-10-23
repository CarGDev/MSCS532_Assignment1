# Insertion Sort Algorithm - Decreasing Order Implementation

## Overview

This project implements the **Insertion Sort Algorithm** to sort arrays in **monotonically decreasing order** (largest to smallest). The implementation provides both in-place and non-destructive sorting variants, along with comprehensive test cases and detailed documentation.

### Key Features

- ✅ **Decreasing Order Sorting**: Sorts arrays from largest to smallest
- ✅ **Two Implementation Variants**: In-place and non-destructive sorting
- ✅ **Comprehensive Test Suite**: Handles edge cases and various input scenarios
- ✅ **Well-Documented Code**: Clear comments and docstrings
- ✅ **Educational Focus**: Demonstrates algorithm concepts with examples

## Architecture

### Algorithm Flow Diagram

```
Input Array: [5, 2, 8, 1, 9, 3]
             ↓
    ┌─────────────────────────────────────┐
    │     Insertion Sort Process          │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 1: Start with element at i=1  │
    │  Current: 2, Sorted: [5]            │
    │  Insert 2 → [5, 2]                  │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 2: Process element at i=2     │
    │  Current: 8, Sorted: [5, 2]         │
    │  Insert 8 → [8, 5, 2]               │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 3: Process element at i=3     │
    │  Current: 1, Sorted: [8, 5, 2]      │
    │  Insert 1 → [8, 5, 2, 1]            │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 4: Process element at i=4     │
    │  Current: 9, Sorted: [8, 5, 2, 1]   │
    │  Insert 9 → [9, 8, 5, 2, 1]         │
    └─────────────────────────────────────┘
             ↓
    ┌─────────────────────────────────────┐
    │  Step 5: Process element at i=5     │
    │  Current: 3, Sorted: [9, 8, 5, 2, 1]│
    │  Insert 3 → [9, 8, 5, 3, 2, 1]      │
    └─────────────────────────────────────┘
             ↓
Output Array: [9, 8, 5, 3, 2, 1]
```

### Core Algorithm Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    Insertion Sort                           │
├─────────────────────────────────────────────────────────────┤
│  Function: insertion_sort_decreasing(arr)                   │
│  Input: Array of comparable elements                        │
│  Output: Array sorted in decreasing order                   │
├─────────────────────────────────────────────────────────────┤
│  Algorithm Steps:                                           │
│  1. Iterate through array starting from index 1             │
│  2. For each element, find its correct position             │
│  3. Shift larger elements to the right                      │
│  4. Insert current element in correct position              │
│  5. Repeat until all elements are processed                 │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Details

### Core Functions

#### 1. `insertion_sort_decreasing(arr)`
- **Purpose**: Non-destructive sorting that returns a new sorted array
- **Parameters**: `arr` (list) - Input array to be sorted
- **Returns**: `list` - New array sorted in decreasing order
- **Space Complexity**: O(n) - Creates a copy of the input array

#### 2. `insertion_sort_decreasing_inplace(arr)`
- **Purpose**: In-place sorting that modifies the original array
- **Parameters**: `arr` (list) - Input array to be sorted (modified)
- **Returns**: `list` - Same array sorted in decreasing order
- **Space Complexity**: O(1) - Sorts in-place

### Algorithm Logic

The key difference from standard insertion sort is the comparison condition:

```python
# Standard insertion sort (ascending):
while j >= 0 and arr[j] > current_element:

# Our implementation (descending):
while j >= 0 and arr[j] < current_element:
```

This ensures that elements are arranged in decreasing order (largest to smallest).

## Complexity Analysis

| Aspect | Complexity | Description |
|--------|------------|-------------|
| **Time Complexity** | O(n²) | Worst case when array is sorted in ascending order |
| **Space Complexity** | O(1) | In-place version uses constant extra space |
| **Best Case** | O(n) | When array is already sorted in descending order |
| **Average Case** | O(n²) | Random order arrays |

## Usage Examples

### Basic Usage

```python
from insertion_sort_decreasing import insertion_sort_decreasing

# Example 1: Basic sorting
arr = [5, 2, 8, 1, 9, 3]
sorted_arr = insertion_sort_decreasing(arr)
print(sorted_arr)  # Output: [9, 8, 5, 3, 2, 1]

# Example 2: In-place sorting
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort_decreasing_inplace(arr)
print(arr)  # Output: [90, 64, 34, 25, 22, 12, 11]
```

### Edge Cases Handled

```python
# Empty array
empty_arr = []
result = insertion_sort_decreasing(empty_arr)
print(result)  # Output: []

# Single element
single = [42]
result = insertion_sort_decreasing(single)
print(result)  # Output: [42]

# Duplicate elements
duplicates = [3, 3, 3, 3]
result = insertion_sort_decreasing(duplicates)
print(result)  # Output: [3, 3, 3, 3]
```

## Running the Program

### Prerequisites
- Python 3.6 or higher

### Execution
```bash
python3 insertion_sort_decreasing.py
```

### Expected Output
The program will run through 7 comprehensive test cases demonstrating:
- Random unsorted arrays
- Already sorted arrays (ascending and descending)
- Edge cases (empty, single element, duplicates)
- Larger arrays for performance demonstration

## Test Cases

The implementation includes comprehensive test cases:

1. **Random Array**: `[5, 2, 8, 1, 9, 3]` → `[9, 8, 5, 3, 2, 1]`
2. **Ascending Order**: `[1, 2, 3, 4, 5]` → `[5, 4, 3, 2, 1]`
3. **Descending Order**: `[5, 4, 3, 2, 1]` → `[5, 4, 3, 2, 1]`
4. **Single Element**: `[1]` → `[1]`
5. **Empty Array**: `[]` → `[]`
6. **Duplicates**: `[3, 3, 3, 3]` → `[3, 3, 3, 3]`
7. **Large Array**: `[64, 34, 25, 12, 22, 11, 90]` → `[90, 64, 34, 25, 22, 12, 11]`

## Educational Value

This implementation serves as an excellent learning resource for:

- **Algorithm Understanding**: Clear demonstration of insertion sort mechanics
- **Sorting Concepts**: Shows how to modify algorithms for different sort orders
- **Code Quality**: Demonstrates good practices in Python programming
- **Testing**: Comprehensive test suite showing edge case handling
- **Documentation**: Well-commented code with clear explanations

## File Structure

```
MSCS532_Assignment1/
├── insertion_sort_decreasing.py    # Main implementation
├── test_insertion_sort.py         # Comprehensive test suite
├── run_tests.py                   # Test runner with various options
├── README.md                      # This documentation
└── LICENSE                        # Project license
```

## Testing

### Running Tests

The project includes a comprehensive test suite with multiple ways to run tests:

#### Quick Tests (Essential functionality)
```bash
python3 run_tests.py --quick
```

#### Full Test Suite
```bash
python3 run_tests.py
```

#### Unit Tests Only
```bash
python3 run_tests.py --unit-only
```

#### Performance Benchmarks
```bash
python3 run_tests.py --benchmark
```

#### Stress Tests
```bash
python3 run_tests.py --stress
```

#### Negative Test Cases
```bash
python3 run_tests.py --negative
```

#### Using unittest directly
```bash
python3 -m unittest test_insertion_sort -v
```

### Test Coverage

The test suite includes **38 comprehensive test cases** covering:

#### ✅ **Functional Tests**
- Basic sorting functionality
- Already sorted arrays (ascending/descending)
- Empty arrays and single elements
- Duplicate elements
- Negative numbers and zero values
- Large numbers and edge cases

#### ✅ **Behavioral Tests**
- Non-destructive sorting (original array unchanged)
- In-place sorting (original array modified)
- Sorting stability (equal elements maintain order)

#### ✅ **Performance Tests**
- Small arrays (10-100 elements)
- Worst-case performance (ascending order)
- Best-case performance (descending order)
- Random arrays with timing measurements

#### ✅ **Stress Tests**
- Edge cases and boundary conditions
- Very large/small numbers
- Mixed data types
- Random large arrays

#### ✅ **Negative Test Cases**
- Invalid input types (None, strings, numbers, dicts, tuples, sets)
- Non-comparable elements (mixed types)
- Nested lists and complex data structures
- Custom objects with/without comparison methods
- Infinity and NaN values
- Unicode strings and special characters
- Boolean values and mixed numeric types
- Very large arrays and deep recursion scenarios

## Contributing

This is an educational project demonstrating insertion sort implementation. Feel free to:
- Add more test cases
- Implement additional sorting algorithms
- Improve documentation
- Optimize the implementation

## License

See LICENSE file for details.
