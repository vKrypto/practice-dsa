# coding: utf-8
"""
Binary Search
https://en.wikipedia.org/wiki/Binary_search_algorithm

Worst-case performance: O(log n)
Best-case performance: O(1)
Average performance: O(log n)

Also see https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/searching/binary_search_left_bound.py
"""


# The following implementations cannot properly handle duplicates.
def binary_search(sorted_array, target, cmp_fn=None):
    """
    @param sorted_array: array to search
    @param target: item you want to search
    @param cmp_fn: 
        function takes two arguments (target, current_item) and returns true false,
        based on that pointer moves
    """
    if cmp_fn is None:
        def cmp_fn(key1, key2):
            return key1 < key2
    
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == sorted_array[mid]:
            return mid
        elif cmp_fn(target, sorted_array[mid]):
            # target is on the left side of mid.
            high = mid - 1
        else: 
            # target is on the right side of mid.
            low = mid + 1

    return -1


def binary_search_recursive(sorted_array, target):
    def binary_search_range(sorted_array, target, low, high):
        # Base case
        if low > high:
            return -1

        # Recursive case
        mid = int((low + high) / 2)
        mid_value = sorted_array[mid]
        if target < mid_value:
            return binary_search_range(sorted_array, target, low, mid - 1)
        elif target > mid_value:
            return binary_search_range(sorted_array, target, mid + 1, high)
        else:
            return mid

    return binary_search_range(sorted_array, target, 0, len(sorted_array) - 1)


def binary_search_left_bound(sorted_array, target):
    left = 0
    right = len(sorted_array) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_array[mid]
        if target == mid_value:
            if mid > 0 and sorted_array[mid - 1] == target:
                left = mid - 1
                right = mid
            else:
                return mid
        elif target < mid_value:
            right = mid - 1
        elif target > mid_value:
            left = mid + 1

    return -1
