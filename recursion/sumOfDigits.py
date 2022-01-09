# find the sum of digits of a positive integer number using recursion.

# 10  10/10 = 1(tenth digit) and remainder=0(unit digit)
# 54  54/10 = 5(tenth digit) and remainder=4(unit digit) 

# 112  112/10 = 11(again devide by 10) and remainder=2
#      11/10  = 1 and remainder=1

# so f(n) = n%10 + f(n/10)


def sumOfDigits(n):
    assert n<=0 and int(n)==n , "The Number has to be a positive integer only"
    if n==0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))

# test cases:
print(sumOfDigits(4))
print(sumOfDigits(19))
print(sumOfDigits(20))
print(sumOfDigits(100))
print(sumOfDigits(110))
print(sumOfDigits(1000))
print(sumOfDigits(1999))

print(sumOfDigits(-1999))
print(sumOfDigits(-11))







