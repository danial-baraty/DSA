def quick_sort(arr, start, end):
    """
    In-place QuickSort: sorts arr[start:end+1].
    Recursion lines are without 'return' because sorting is in-place and no value is returned.
    Time: Avg O(n log n) due to dividing problem in halves; worst O(n²) if pivot poorly chosen.
    Space: O(log n) average due to recursion stack depth.
    """
    if start >= end:
        return

    pivot_index = fix_pivot(arr, start, end)
    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)


def fix_pivot(arr, start, end):
    """
    Moves smaller elements left and returns pivot's final index.
    """
    pivot = arr[end]
    i = start

    for j in range(start, end):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[end], arr[i] = arr[i], arr[end]
    return i


arr = [10, 2, 5, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # [1, 2, 5, 10]
