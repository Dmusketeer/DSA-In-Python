# largest number in a list
# Input: list1 = [10, 20, 4]
# Output: 20
# Input: list2 = [20, 10, 20, 4, 100]
# Output: 100


def largest_number(lst):
    max = lst[0]
    for i in lst:
        if i >= max:
            max = i
    return max


if __name__ == '__main__':
    # lst = [20, 10, 20, 4, 100]
    lst = [10, 20, 4]
    print(largest_number(lst))
