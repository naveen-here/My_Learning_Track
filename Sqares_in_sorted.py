def sorted_sqare(arr):
    sorted_arr=[x**2 for x in arr]
    sorted_arr.sort()
    return sorted_arr
def sorted_squared(arr):
    squared_arr = [x ** 2 for x in arr]  # Square each element
    squared_arr.sort()  # Sort the squared values
    return squared_arr

# Example usage:
input_array = [1, 2, 3, 4, 5]
sorted_sqare(input_array)
