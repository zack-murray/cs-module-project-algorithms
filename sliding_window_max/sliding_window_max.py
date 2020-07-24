
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# O(n), maybe O(n2) due to max? Because it loops through once and adds each max
# window value to a new list and returns it?
def sliding_window_max(nums, k):
    # Index
    i = 0
    # Stored max of each window in array
    arr = []
    # While index + (window-1) < len of array
    # (So window doesn't extend past last element)
    while i + (k-1) < len(nums):
        # Append the max number in the window to our new array
        arr.append(max(nums[i:(i+k)]))
        # Increment the index
        i += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
