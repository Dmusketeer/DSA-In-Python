# Find the maximum and minimum element of an array
def FindMinAndMax(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return (min, max)


if __name__ == "__main__":
    arr = [12, 34, 5, 2, 66]
    print(FindMinAndMax(arr))

# timecomplexity = O(n)
# spacecomplexity = O(1)
