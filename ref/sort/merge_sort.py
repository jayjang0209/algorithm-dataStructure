# Mergesort


# Time complexity: O(n * log(n))
# Space complexity: O(n)

def merge_sort(arr):
    # Sorts array A[0 ... n-1] by recursive mergesort
    # Input: array A[0 ... n-1] of orderable elements
    # output: array A[0 ... n-1] sorted in nondecreasing order

    # Base case: if the arr length is 0 or 1
    if len(arr) <= 1:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left = arr[:mid]  # mid not included
    right = arr[mid:]

    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    # Merges two sorted arrays into one sorted array
    # Input: left[0...p-1], right[0...q-1] sorted
    # Output: sorted array A[0..p + q -1]
    result = []
    left_index = 0
    right_index = 0

    # Iterate through both lists until one is empty
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append the remaining elements, if any, from the non-empty list
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    unsorted_list = [5, 2, 3, -1, 9, 15, -7]
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


if __name__ == "__main__":
    main()

