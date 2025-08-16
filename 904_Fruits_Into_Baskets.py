from collections import defaultdict

def totalFruit(fruits):
    """
    Calculates the maximum number of fruits that can be collected from a row of trees
    using two baskets that can each hold only one type of fruit.

    This uses a sliding window approach to find the longest contiguous subarray
    with at most two distinct fruit types.

    Args:
        fruits (List[int]): An array where each element represents a type of fruit on a tree.

    Returns:
        int: The maximum number of fruits that can be collected.
    
    Time Complexity: O(N), where N is the length of the fruits array.
    Space Complexity: O(1), because the dictionary stores at most 2 keys.
    """

    count = defaultdict(int)  # Tracks count of fruit types in the current window
    left = 0
    max_len = 0

    for right in range(len(fruits)):
        count[fruits[right]] += 1  # Include current fruit in the window

        # If more than 2 types, shrink the window from the left
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]  # Remove fruit type if count is zero
            left += 1  # Move window forward

        # Update max window size
        max_len = max(max_len, right - left + 1)

    return max_len
