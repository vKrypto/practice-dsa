# coding: utf-8
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
