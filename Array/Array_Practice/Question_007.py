# list = test_list = [1, 6, 3, 5, 3, 4]

# Input: 3  # Check if 3 exist or not.
# Output: True

# Input: 7  # Check if 7 exist or not.
# Output: False

# Approach 1:
def element_exist(list, element):
    return element in list

# Approach 2:


def element_exist(list, element):
    for item in range(len(list)):
        return list[item] == element

# Approach 3:


def element_exist(list, element):
    try:
        list.index(element)
        return True
    except ValueError:
        return False


# driver code
if __name__ == "__main__":
    lst = [1, 6, 3, 5, 3, 4]
    ele = 7
    print(element_exist(lst, ele))
