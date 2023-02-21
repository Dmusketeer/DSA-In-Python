# Array

- An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. 

- Types of arrays : 
One dimensional array (1-D arrays)
Multidimensional array

- Advantages of using arrays: 
    - Arrays allow random access to elements. This makes accessing elements by position faster.
    - Arrays have better cache locality which makes a pretty big difference in performance.
    - Arrays represent multiple data items of the same type using a single name.

- Disadvantages of using arrays: 
    - You can’t change the size i.e. once you have declared the array you can’t change its size because of static memory allocation. 
    - Here Insertion(s) and deletion(s) are difficult as the elements are stored in consecutive memory locations and the shifting operation is costly too.

- Applications on Array
    - Array stores data elements of the same data type.
    - Arrays are used when the size of the data set is known.
    - Used in solving matrix problems.
    - Applied as a lookup table in computer.
    - Databases records are also implemented by the array.
    - Helps in implementing sorting algorithm.
    - The different variables of the same type can be saved under one name.
    - Arrays can be used for CPU scheduling.
    - Used to Implement other data structures like Stacks, Queues, Heaps, Hash tables, etc.


# Python Arrays

- Python does not have built-in support for Arrays, but Python Lists can be used instead.
  


## Creating a Array
- Array in Python can be created by importing array module. array(data_type, value_list) is used to create an array with data type and value list specified in its arguments. 
```py

# Creation of Array
 
# importing "array" for array creations
import array as arr
 
# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# Time Complexity: O(1)
# Auxiliary Space: O(n)

```

## Adding Elements to a Array
- Elements can be added to the Array by using built-in <b>insert()</b> function. Insert is used to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end, or any given index of array.
- <b>append()</b> is also used to add the value mentioned in its arguments at the end of the array.

```py

# importing "array" for array creations
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3])
 
# inserting array using
# insert() function
a.insert(1, 4)
 
# adding an element using append()
b.append(4.4)

```

## Accessing elements from the Array
- In order to access the array items refer to the index number. Use the index operator [ ] to access an item in a array. The index must be an integer. 

```py
# importing array module
import array as arr
 
# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])
 
# accessing element of array
print("Access element is: ", a[0])
```