# Multiply all numbers in the list
# Input: list1 = [3, 2, 4]
# Output: 24


def multiply_all_ele(lst):
    mul = 1
    for i in lst:
        mul = mul*i
    return mul


if __name__ == '__main__':
    list1 = [3, 2, 4]
    print(multiply_all_ele(list1))
