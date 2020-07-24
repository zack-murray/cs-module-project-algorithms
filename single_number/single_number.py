'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Loop through the array counting each number
    for i in range(1, len(arr)):
        # If the count ends at 1, return it
        if arr.count(i) == 1:
            return i

# XOR bitwise approach that I thought looked interesting
# takes in array and length of array
def find_single(arr, n):
    # Instantiate the result counter
    result = arr[0]
    # Loop through the array, counting from beginning 
    for i in range(1, n):
        # ^ is xor operator, duplicates cancel eachother out (0)
        # non-duplicates keep their value
        result = result ^ arr[i]
    
    return result

# try dictionary approach / count



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")