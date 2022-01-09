# find the sum of digits of a positive integer number using recursion.

# 10  10/10 = 1(tenth digit) and remainder=0(unit digit)
# 54  54/10 = 5(tenth digit) and remainder=4(unit digit) 

# 112  112/10 = 11(again devide by 10) and remainder=2
#      11/10  = 1 and remainder=1

# so f(n) = n%10 + f(n/10)


def sumOfDigits(n):
    if n==0:
        return 0
    else:
        return n%10 + sumOfDigits(n//10)

# test cases:
print(sumOfDigits(4))
print(sumOfDigits(10))
print(sumOfDigits(19))
print(sumOfDigits(20))
print(sumOfDigits(100))
print(sumOfDigits(110))
print(sumOfDigits(1000))
print(sumOfDigits(1999))




