def merge_sort(arr: list[int]) -> list[int]:
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    sorted_array = []
    left_half_ptr = right_half_ptr = 0  # clearer pointer names

    while left_half_ptr < len(left_half) and right_half_ptr < len(right_half):
        if left_half[left_half_ptr] <= right_half[right_half_ptr]:
            sorted_array.append(left_half[left_half_ptr])
            left_half_ptr += 1
        else:
            sorted_array.append(right_half[right_half_ptr])
            right_half_ptr += 1

    # Append any remaining elements from either half
    sorted_array.extend(left_half[left_half_ptr:])
    sorted_array.extend(right_half[right_half_ptr:])

    return sorted_array
