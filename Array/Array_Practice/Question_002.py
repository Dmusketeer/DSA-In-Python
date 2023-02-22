# Write a program to reverse an Array

# using another array
def reverse_array(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr[len(arr)-i-1])
    return newArr

# without using another array


def reverse_array_without_2ndArray(arr):
    return arr[::-1]

# driver code


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(reverse_array(arr))
    arr1 = [10, 20, 30, 40, 50]
    print(reverse_array_without_2ndArray(arr1))
