class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        current_len = 0
        maxi = 0

        for num in nums:
            if num == max_val:
                current_len += 1
                maxi = max(maxi, current_len)
            else:
                current_len = 0
        return maxi

    # Follow-Up question
    # return longest subarray with maximum bitwise AND
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        current_len = 0
        maxi = 0
        start = 0
        best = 0

        for i, num in enumerate(nums):
            if num == max_val:
                if current_len == 0:
                    start = i
                current_len += 1
                if current_len > maxi:
                    maxi = current_len
                    best = start
            else:
                current_len = 0
        return nums[best:best + maxi]