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
        if arr[left] + arr[right] > sum:
            right -= 1
        elif arr[left] + arr[right] < sum:
            left += 1
        elif arr[left] + arr[right] == sum:
            print("Values of the pair are", arr[left], '&', arr[right])
            right -= 1
            left += 1


rr = [5, 7, 4, 3, 9, 8, 19, 21]
sum = 12
print(twosum(arr, sum))