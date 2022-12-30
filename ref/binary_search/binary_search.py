"""
Binary Search
"""


def binary_search(arr, x):
    # Set the left and right indices
    left = 0
    right = len(arr) - 1

    # Perform the binary search
    while left <= right:
        # Calculate the midpoint
        mid = (left + right) // 2

        # Check if the element at the midpoint is equal to x
        if arr[mid] == x:
            return mid

        # If x is smaller, search the left half of the array
        elif arr[mid] > x:
            right = mid - 1

        # If x is larger, search the right half of the array
        else:
            left = mid + 1

    # If the element is not found, return -1
    return -1


"""
find a character in a string in Python
"""


def find_char(s: str, c: str) -> int:
    # Convert the string to a list
    s_list = list(s)

    # Set the left and right indices
    left = 0
    right = len(s_list) - 1

    # Perform the binary search
    while left <= right:
        # Calculate the midpoint
        mid = (left + right) // 2

        # Check if the element at the midpoint is equal to c
        if s_list[mid] == c:
            return mid

        # If c is lexicographically smaller, search the left half of the list
        elif s_list[mid] > c:
            right = mid - 1

        # If c is lexicographically larger, search the right half of the list
        else:
            left = mid + 1

    # If the character is not found, return -1
    return -1
