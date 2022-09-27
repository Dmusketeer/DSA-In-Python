# Arrays Rotation: The rotation of arrays simply means to shift the array elements to the specified positions. 

# Program for array rotation
# explaination : Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.

# Examples:  

# Input: arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=3
# Output: 6 7 1 2 3 4 5

def leftRotate(arr,d,n):
    k=arr.index(d)
    tempArr=[]
    tempArr=arr[k+1:]+arr[0:k+1]
    return tempArr

# driver code
if __name__=='__main__':
    Arr=[1, 2, 3, 4, 5, 6, 7]
    d=2
    N=len(Arr)
    mArr=leftRotate(Arr,d,N)
    for i in mArr:
        print(i,end=" ")

# Time complexity : O(n) 