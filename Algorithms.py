"""These are 10 algorithms that are common, but by no means the big 10. It really depends
on the situation. There is a book called `Learning Algorithms` by O'Reilly publishing that
goes into a lot of detail about this and details hash tables as well - all of its code examples
are in Python too!"""

# Caveat 1. The input data must be sorted in ascending or descending order. Binary search relies on the sorted nature of the 
# data to eliminate half of the remaining elements with each iteration. If the data is not sorted, binary search will 
# not work correctly.

# Caveat 2. Unique or handling duplicates: While binary search can work with data containing duplicates, it is essential to 
# understand how it behaves in such cases. If you are searching for a specific value and there are duplicates in the data, 
# binary search may not return the index of the first occurrence. If you need the index of the first occurrence or need to 
# handle duplicates in a specific manner, you should modify the binary search algorithm accordingly.

# O(log)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # target found, return its index
        elif mid_val < target:
            low = mid + 1  # search in the right half
        else:
            high = mid - 1  # search in the left half

    return -1  # target not found, return -1


# Example usage:
arr = [1, 3, 4, 6, 8, 9, 11, 13, 16, 18, 20]
target = 11

result = binary_search(arr, target)
if result != -1:
    print("Binary Search Example Output: " + f"Element {target} found at index {result}")
else:
    print("Binary Search Example Output: " + f"Element {target} not found in the array")
