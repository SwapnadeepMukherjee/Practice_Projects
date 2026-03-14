print("Shallow Copy starts here")

import copy

# Example with a list containing another list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Creating a shallow copy
shallow = copy.copy(original_list)
# Or using slice notation: shallow = original_list[:]
# Or using list(): shallow = list(original_list)

# They're different objects
print(original_list is shallow)  # False

# But the inner lists are the same objects
print(original_list[0] is shallow[0])  # True

# Modifying inner list affects both
shallow[0][0] = 999
print(original_list)  # [[999, 2, 3], [4, 5, 6], [7, 8, 9]]
print(shallow)        # [[999, 2, 3], [4, 5, 6], [7, 8, 9]]

# But adding new elements to outer list doesn't affect the other
shallow.append([10, 11, 12])
print(len(original_list))  # 3
print(len(shallow))         # 4

# ----------------------------------------->

print("Deep Copy starts here")
import copy

# Same starting point
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Creating a deep copy
deep = copy.deepcopy(original_list)

# They're different objects
print(original_list is deep)  # False

# The inner lists are ALSO different objects
print(original_list[0] is deep[0])  # False

# Modifying inner list only affects the copy
deep[0][0] = 999
print(original_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(deep)           # [[999, 2, 3], [4, 5, 6], [7, 8, 9]]

# But adding new elements to outer list doesn't affect the other
deep.append([10, 11, 12])
print(len(original_list))  # 3
print(len(shallow))         # 4