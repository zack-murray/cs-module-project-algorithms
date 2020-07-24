'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Instantiate new array 
    merged_array = []
    # Loop through array
    for i in arr:
        # Look for all non-zero values
        if i != 0:
            # Put them into merged_array
            merged_array.append(i)
    # Loop through the array again
    for i in arr:
        # Look for all zero values
        if i == 0:
            # Append them to the end of merged_array
            merged_array.append(i)
    
    return merged_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")