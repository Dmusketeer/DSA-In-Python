# count the number of occurrences of x in the given list.
# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3
# Explanation: 10 appears three times in given list.


def occurrence_of_x(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count


if __name__ == '__main__':
    lst = [15, 6, 7, 10, 20, 20, 10, 28, 10]
    x = 20
    print(occurrence_of_x(lst, x))
