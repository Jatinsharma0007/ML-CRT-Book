def max_consecutive_sum(nums, k):
    if k > len(nums):
        raise ValueError("k cannot be larger than the list length")
    if not nums or k == 0:
        return 0
    
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Test the function
def test_max_consecutive_sum():
    # Test cases
    test_lists = [
        ([1, 2, 3, 4, 5], 3),  # Standard case
        ([1, 1, 1, 1, 1], 2),  # Uniform list
        ([-1, -2, -3, -4, -5], 2),  # Negative numbers
        ([10, 20, 30, 40, 50], 1),  # Single element window
    ]
    
    for nums, k in test_lists:
        result = max_consecutive_sum(nums, k)
        print(f"List: {nums}, k: {k}, Max Consecutive Sum: {result}")

# Run the test function
test_max_consecutive_sum()
