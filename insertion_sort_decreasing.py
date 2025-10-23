def insertion_sort_decreasing(arr):
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        current_element = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] < current_element:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = current_element
    return sorted_arr


def insertion_sort_decreasing_inplace(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < current_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr


def print_array(arr, label="Array"):
    print(f"{label}: {arr}")


def main():
    print("Insertion Sort Algorithm - Decreasing Order")
    print("=" * 50)
    test_arrays = [
        [5, 2, 8, 1, 9, 3],
        [1, 2, 3, 4, 5],  # Already sorted in ascending order
        [5, 4, 3, 2, 1],  # Already sorted in descending order
        [1],              # Single element
        [],               # Empty array
        [3, 3, 3, 3],     # All same elements
        [64, 34, 25, 12, 22, 11, 90]
    ]
    for i, test_arr in enumerate(test_arrays, 1):
        print(f"\nTest Case {i}:")
        print_array(test_arr, "Original")
        sorted_arr = insertion_sort_decreasing(test_arr)
        print_array(sorted_arr, "Sorted (decreasing)")
        print_array(test_arr, "Original (unchanged)")
        test_arr_copy = test_arr.copy()
        insertion_sort_decreasing_inplace(test_arr_copy)
        print_array(test_arr_copy, "In-place sorted")
        print("-" * 30)

if __name__ == "__main__":
    main()
