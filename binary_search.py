
# Since the array is sorted, we either increment start (discarding the left half) or decrement end (discarding the right half) in each step. This narrows the search range until start > end.
# As the core operation is updating start and end indices, the algorithm can be implemented either iteratively (using a loop) or recursively (via function calls for new ranges).

def rec_binary_search(arr, x, start, end):
    """
    Recursive binary search on a sorted list.

    Returns the index of x if found; otherwise, None.
    Assumes 'arr' is already sorted.
    """
    if start > end:
        return None
    
    mid = (start + end) // 2

    if x == arr[mid]:
        return mid
    
    elif x < arr[mid]:
        return rec_binary_search(arr, x , start, mid - 1)

    else:
        return rec_binary_search(arr, x,  mid + 1, end)


# my_arr = [1, 8, 9, 10, 21, 27]
# my_arr.sort()
# index = rec_binary_search(my_arr, 27, 0, len(my_arr) - 1)
# print(index)


def iterative_binary_search(arr, x):
    """
    Perform iterative binary search on a sorted copy of the list.
    Returns the index of x if found, otherwise -1.
    """
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1



# my_arr = [1, 8, 9, 6, 21, 27]
# index = iterative_binary_search(my_arr, 9)
# print(index)
# print(my_arr)
