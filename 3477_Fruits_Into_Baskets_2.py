from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        Determines the number of fruit types that cannot be placed into baskets
        based on the rules:
        
        - Each fruit must go into the leftmost available basket that can hold it.
        - Each basket can be used only once.
        
        Parameters:
        fruits (List[int]): List of fruit quantities.
        baskets (List[int]): List of basket capacities.
        
        Returns:
        int: Number of unplaced fruit types.
        """
        n = len(fruits)
        used = [False] * n  # To track used baskets
        count = 0  # Unplaced fruits counter

        # Iterate through each fruit
        for i in range(n):
            placed = False
            # Try to place the fruit in the leftmost valid basket
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True  # Mark basket as used
                    placed = True
                    break
            if not placed:
                count += 1  # Could not place the fruit

        return count


# Optional: Test cases to verify output
if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]))  # Output: 1
    print(sol.numOfUnplacedFruits([3, 6, 1], [6, 4, 7]))  # Output: 0
