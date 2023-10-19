# Find out pairs with given sum in an array in python.
# Time complexity O(n log n).
# Asked in FACEBOOK,AMAZON.

# Solution - https://www.youtube.com/watch?v=J-88ssjEv9o
# using two pointer approach -

def twosum(arr, sum):
    sorted_arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    final_array = []
    while left <= right:
        if sorted_arr[left] + sorted_arr[right] > sum:
            right -= 1

        elif sorted_arr[left] + sorted_arr[right] < sum:
            left += 1
        elif sorted_arr[left] + sorted_arr[right] == sum:
            final_array.append([sorted_arr[left], sorted_arr[right]])
            right -= 1
            left += 1
    print("Values of the pair are", final_array)


arr = [8, 4, 2, 6, 10, 12, 18, 15, 16, 24]
sum = 12
twosum(arr, sum)


# Reference articles for further practice and learning -
# 1. https://www.geeksforgeeks.org/count-pairs-with-given-sum/
# 2. https://www.youtube.com/watch?v=bvKMZXc0jQU
# 3. https://www.geeksforgeeks.org/print-all-pairs-with-given-sum/

# Approach - 2:

# Python 3 implementation
# of simple method to find
# print pairs with given sum.

# Returns number of pairs
# in arr[0..n-1] with sum
# equal to 'sum'


def printPairs(arr, n, sum):
    count = 0
    final_arary = []

    # Consider all possible
    # pairs and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")
    final_arary.append([arr[i], arr[j]])


# Driver Code
printPairs(arr=[1, 5, 7, -1, 6], n=len(arr), sum=6)