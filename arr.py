def sorted_squared(arr):
    squared_arr = [x ** 2 for x in arr]  # Square each element
    squared_arr.sort()  # Sort the squared values
    return squared_arr

# Example usage:
input_array = [1, 2, 3, 4, 5]