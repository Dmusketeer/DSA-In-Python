# find second largest number in a list
# Input: list1 = [10, 20, 4]
# Output: 10

# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70


# Find Second largest element in an array

# Naive approach:
# def second_largest_element(arr):
#     if len(arr) < 2:
#         print("Invalid input")
#         return
#     arr.sort()
#     return f"Second largest element is : {arr[-2]}"


def second_largest_element(arr):
    f = s = min(arr)
    for i in range(len(arr)):
        if arr[i] > f:
            s = f
            f = arr[i]
        elif arr[i] < f and arr[i] > s:
            s = arr[i]
    return f"Second largest element is : {s}"


# Time Complexity: O(n).

if __name__ == "__main__":
    arr = [70, 11, 20, 4, 100]
    print(second_largest_element(arr))
