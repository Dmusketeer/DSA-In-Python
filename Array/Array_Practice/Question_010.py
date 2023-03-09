# Find sum and average of List in Python
# Input: [4, 5, 1, 2, 9, 7, 10, 8]
# Output:sum = 46, average = 5.75

def find_sum_average(list):
    sum = 0
    for i in lst:
        sum = sum+i
        avg = sum/len(lst)
    opt = [sum, avg]
    return opt


if __name__ == '__main__':
    lst = [4, 5, 1, 2, 9, 7, 10, 8]
    print("Sum:", find_sum_average(lst)[0])
    print("Average:", find_sum_average(lst)[1])
