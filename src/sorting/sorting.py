# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    merged_arr = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            merged_arr.append(right[r])
            r += 1
        else:
            merged_arr.append(left[l])
            l +=1
    merged_arr.extend(left[l:])
    merged_arr.extend(right[r:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    mid = len(arr)//2
    if mid < 1:
        return arr
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

