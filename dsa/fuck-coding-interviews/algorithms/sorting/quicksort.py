# coding: utf-8
"""
Quick Sort
https://en.wikipedia.org/wiki/Quicksort

Worst-case performance: O(n^2)
Best-case performance: O(n * log n)
Average performance: O(n * log n)
"""


# This implementation takes extra space but is more faster than the in-place version
def quicksort(arr):
    # Base case:
    # The list is considered sorted if it's empty or there is only one item.
    if len(arr) <= 1:
        return arr

    # Recursive case:
    # Select the middle as the pivot,
    # partition items into tree sublists by whether they are equal to, less than, or greater than the pivot,
    # sort three sublists recursively, and concatenate them.
    pivot = arr[len(arr) // 2]
    left_list = []
    right_list = []
    center_list = []
    for item in arr:
        if item < pivot:
            left_list.append(item)
        elif item > pivot:
            right_list.append(item)
        # NOTE: There might be duplicates of the pivot.
        elif item == pivot:
            center_list.append(item)

    return quicksort(left_list) + center_list + quicksort(right_list)


# https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
# https://stackabuse.com/quicksort-in-python/
def quicksort_in_place(arr):
    # Partition is to move all items that less than the pivot to the left side of the pivot,
    # and move all items that greater than the pivot to the right side of the pivot
    # As a result, the pivot is in its final position,
    # but items in both sides of the pivot don't necessarily end up sorted
    def partition(arr, start, end):
        # Select the first item as the pivot,
        # So the left cursor starts from the next index of the pivot
        pivot_index = start
        pivot = arr[pivot_index]
        left = start + 1
        right = end

        while True:
            # If the current item is less than or equal to the pivot,
            # it's in the proper side (left side of the pivot),
            # then we move the left cursor right to the next element
            while left <= right and arr[left] <= pivot:
                # The left cursor stops at the item which is greater than the pivot
                left = left + 1

            # The right cursor behaves oppositely to the left cursor
            while left <= right and arr[right] >= pivot:
                right = right - 1

            # We swap both items the left and right cursor found that are in the wrong side,
            # In the end, we move all items to their proper side of the pivot
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                break

        # We swap the pivot with the right cursor,
        # so the pivot ends up in the correct index
        if pivot_index != right:
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            pivot_index = right

        return pivot_index

    def quicksort_range(arr, start, end):
        # Base case
        # The array of size 0 or 1 which (start, end) is (0, -1) or (0, 0)
        if start >= end:
            return arr

        # Recursive case
        pivot_index = partition(arr, start, end)
        quicksort_range(arr, start, pivot_index - 1)
        quicksort_range(arr, pivot_index + 1, end)
        return arr

    return quicksort_range(arr, 0, len(arr) - 1)
