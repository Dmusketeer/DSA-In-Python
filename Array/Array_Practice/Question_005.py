# Input: List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output: [19, 65, 23, 90]

# Input: List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output: [1, 5, 3, 4, 2]


def swap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


if __name__ == '__main__':
    # lst = [23, 65, 19, 90]
    # pos1 = 1
    # pos2 = 3
    lst = [1, 2, 3, 4, 5]
    pos1 = 2
    pos2 = 5
    print(swap(lst, pos1-1, pos2-1))
