# write a Python program to swap first and last element of the list.
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]


# without using another array

# approach_1
# def swap_elements(list):
#     list[0], list[-1] = list[-1], list[0]
#     return list


# approach_2
def swap_elements(list):
    start, *middle, end = list
    list = [end, *middle, start]
    return list


if __name__ == '__main__':
    lst = [12, 35, 9, 56, 24]
    print(swap_elements(lst))
