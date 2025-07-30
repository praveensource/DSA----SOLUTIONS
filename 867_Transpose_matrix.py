#  Intuition
# The transpose of a matrix can be obtained by swapping its rows and columns. We iterate through each element of the original matrix and fill the corresponding position in the transposed matrix.

# Approach
# Determine the number of rows (row) and columns (col) in the original matrix.
# Create a new matrix arr with dimensions col x row.
# Iterate through each element of the original matrix, assigning it to the corresponding position in the transposed matrix.
# Return the transposed matrix.
# Complexity
# Time Complexity: O(m * n) where m and n are the number of rows and columns in the matrix.
# Space Complexity: O(m * n) for the transposed matrix.
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0] * rows for _ in range(cols)]


        for c in range(cols):
            for r in range(rows):
                result[c][r] = matrix[r][c]
        return result
       
