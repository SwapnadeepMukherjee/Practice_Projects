# Problem - 1 - WAP to generate an m*n dimension array with diagonals set to 1:

# Sample Input - m X n - 2 * 2

# Sample output -
# [1 0
#  0 1]

# Approach during interview -
#
# # # 1. First we create an array;
# #
# m = 3
# n = 3
# array = []
#
# # # 2. then i need insert elements index row-wise;
# #
# for i in range(m):
#     for j in range(n):
#         if i == j:
#             array.append(1)
#             # array[i][j] = 1.
#
#         else:
#             array.append(0)
#             # array[i][j] = 0
# #         return array
# print(array)

# Approach using numpy -

import numpy as np


def generate_array(m, n):
    """Generates an m*n dimension array with diagonals set to 1.

  Args:
    m: The number of rows in the array.
    n: The number of columns in the array.

  Returns:
    A numpy array of shape (m, n) with diagonals set to 1.
  """

    array = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if i == j or i + j == n - 1:
                array[i][j] = 1
    return array


# Example usage:

array = generate_array(5, 5)
print(array)