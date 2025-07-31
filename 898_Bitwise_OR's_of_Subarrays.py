class Solution:
    # approach - 1 --
    # let's find all the subarrays then find bitwise or between them also apply set operation.
    # TC - O(n**2)
    # So instead of brute-forcing every subarray (which would be O(n²)),we track how OR values evolve as we move through the array.

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        curr = set()

        for num in arr:
            next_curr = {num}
            for prev in curr:
                next_curr.add(prev | num)
            curr = next_curr
            result.update(curr)
        return len(result)
    
    # TC --- > O(N)
    # SC --- > O(N)