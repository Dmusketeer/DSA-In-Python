# write a Python code to find the Maximum of these two numbers.
# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1

def maxofTwoNumbers(a, b):
    max = 0
    if a > b:
        max = a
    else:
        max = b
    # or
    # x = [a, b]
    # x.sort()
    return x[-1]


if __name__ == '__main__':
    n1 = -1
    n2 = -4
    print(maxofTwoNumbers(n1, n2))
