# Reversing a list using two-pointer approach
# Input: list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4]

def reverse_array(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left = left+1
        right = right-1
    return arr


if __name__ == "__main__":
    lst = [4, 5, 6, 7, 8, 9]
    print(reverse_array(lst))

# Time Complexity: O(N)
# Auxiliary Space: O(1)
