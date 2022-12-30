def isUnique(s: str, c: str) -> bool:
    # Convert the string to a list and sort it
    s_list = list(s)
    s_list.sort()

    # Use binary search to find the index of the character in the sorted list
    left = 0
    right = len(s_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if s_list[mid] == c:
            # Check if the character occurs more than once
            if (mid > 0 and s_list[mid - 1] == c) or (mid < len(s_list) - 1 and s_list[mid + 1] == c):
                return False
            else:
                return True
        elif s_list[mid] < c:
            left = mid + 1
        else:
            right = mid - 1

    # Return False if the character is not found in the list
    return False
