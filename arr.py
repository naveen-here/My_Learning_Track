def sorted_sq(arr):
    sorted_arr=[ x**2 for x in arr]
    sorted_arr.sort()
    return sorted_arr
arr=[1,2,3,4,5]
sorted_sq(arr)
print("array")
