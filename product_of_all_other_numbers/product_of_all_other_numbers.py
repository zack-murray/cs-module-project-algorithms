'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Keep a running count of the multipled values
    x = 1
    # Loop through the array
    for i in arr:
        # Add to the running count by sequentially multiplying
        # arr = [1, 2, 3, 4, 5]
        # 1 x 2 = 2 x 2 = 4 x 3 = 12 x 4 = 48 x 5 = 240 
        x *= i
    # Divide the total seperately by each given number in the array
    # and return the totals
    # 240/1 = 240, 240/2 = 120, 240/3 = 80, 240/4 = 60, 240/5 = 48
    # [240, 120, 80, 60, 48]
    return [x / i for i in arr]

# def product_of_all_other_numbers(arr):
#     # Array to contain multiplied products
#      product_array = []
#      # Get index, value tuples for every value in array
#      for idx, val in enumerate(arr):
#          # Running total of muliplication process, to be sent to product array
#          running_count = 1
#          # Loop index and values
#          for i, n in enumerate(arr):
#              # If the two indexes dont match
#              if i != idx:
#                  # Sequentially multiply that number with all others in the array
#                  # whoms indexes dont match
#                  running_count *= n
#         # Append the total multiplied value to the product array
#          product_array.append(running_count)
#      return product_array

# import math

# def product_of_all_other_numbers(lst):
#     data = []
#     for i in range(len(lst)):
#         data.append(math.prod(lst[:i] + lst[i+1:]))
#     return data

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
