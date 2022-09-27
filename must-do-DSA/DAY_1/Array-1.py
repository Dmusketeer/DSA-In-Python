# The array can be handled in python by a module named “array“.
# They can be useful when we have to manipulate only specific data type values.

# Operations on Array :

        # 1. array(data type, value list):- 
        # This function is used to create an array with data type and value list specified in its arguments.
        # i=int,f=float
        
        #2. append(): add the value at the end of the array.
        # 3.insert(i,x):add the value(x) at the ith position.
# Example:


# Python code to demonstrate the working of
# array(), append(), insert()
# importing "array" for array operations
import array
# initializing array with array values
# initializes array with signed integers
myArr=array.array('i',[1,3,4])
# printing original array
for i in range(0,len(myArr)):
    print(myArr[i],end=" ")

print('\n')
# using append() to insert new value at end

myArr.append(5)
# printing appended array
for i in range(0,len(myArr)):
    print(myArr[i],end=" ")

     
print('\n')
# using insert() to insert value at specific position
# inserts 2 at 1st(array is 0 index based) position

myArr.insert(1,2)
for i in range(0,len(myArr)):
    print(myArr[i],end=" ")

print("\n")
# 4. pop(): This function removes the element at the position mentioned in its argument and returns it.
# 5. remove():- This function is used to remove the first occurrence of the value mentioned in its arguments.

# using pop() to remove element at 3nd position

print(myArr.pop(3))
# printing array after popping
for i in range(0,len(myArr)):
    print(myArr[i],end=" ")

print("\n")

# 6. index():- This function returns the index of the first occurrence of the value
# 7. reverse():- This function reverses the array.

# using index() to print index of 1st occurrence of 5

print(myArr.index(5))

print("\n")
# print(myArr.reverse()) #return none
for i in range(0,len(myArr)):
    print(myArr[i],end=" ")

