# Find out pairs with given sum in an array in python.
# Time complexity O(n log n).
# Asked in FACEBOOK,AMAZON.

# Solution - https://www.youtube.com/watch?v=J-88ssjEv9o
# using two pointer approach -

def twosum(arr, sum):
    sorted_arr = sorted(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        if sorted_arr[left] + sorted_arr[right] > sum:
            right -= 1

        elif sorted_arr[left] + sorted_arr[right] < sum:
            left += 1
        elif sorted_arr[left] + sorted_arr[right] == sum:
            print("Values of the pair are", sorted_arr[left], '&', sorted_arr[right])
            right -= 1
            left += 1


arr = [8, 4, 2, 6, 10, 12, 18, 15, 16, 24]
sum = 12
twosum(arr, sum)