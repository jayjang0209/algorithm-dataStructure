"""
Deque in Python

https://www.geeksforgeeks.org/deque-in-python/
"""
"""
 Appending Items Efficiently
"""
# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

"""
Popping Items Efficiently
"""
# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([6, 1, 2, 3, 4])
print("deque: ", de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)

"""
Accessing Items in a deque
"""
# Python code to demonstrate working of
# insert(), index(), remove(), count()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print("The number 4 first occurs at a position : ")
print(de.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position
de.insert(4, 3)

# printing modified deque
print("The deque after inserting 3 at 5th position is : ")
print(de)

# using count() to count the occurrences of 3
print("The count of 3 in deque is : ")
print(de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)

# printing modified deque
print("The deque after deleting first occurrence of 3 is : ")
print(de)