# prerequisites
# 807_Transpose_Matrix
# Here we do the transpose of a matrix then reverse each row then we got the matrix rotated to 90 degrees.
TC = O(m*n)
SC = O(1) -- we haven't used any extra spaces

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        
        # reverse each row

        for i in range(n):
            matrix[i].reverse()

        