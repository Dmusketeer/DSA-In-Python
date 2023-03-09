# find smallest number in a list
# Input: list1 = [10, 20, 4]
# Output: 4

# Input: list2 = [20, 10, 20, 1, 100]
# Output: 1
def smallest_number(lst):
    num = lst[0]
    for i in lst:
        if i <= num:
            num = i
    return num


if __name__ == '__main__':
    list1 = [20, 10, 20, 2, 100]
    print(smallest_number(list1))
