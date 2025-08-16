def shiftGrid(grid, k):
    """
    Shifts elements of a 2D grid to the right by k times, as per given rules.

    Args:
        grid (List[List[int]]): 2D list representing the grid.
        k (int): Number of times to perform the shift.

    Returns:
        List[List[int]]: Grid after k shifts.

    Time Complexity: O(k * m * n)
    Space Complexity: O(m * n)
    """

    m, n = len(grid), len(grid[0])
    count = 0

    while count < k:
        new_grid = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Compute next position after 1 shift
                if j == n - 1:
                    if i == m - 1:
                        new_grid[0][0] = grid[i][j]
                    else:
                        new_grid[i + 1][0] = grid[i][j]
                else:
                    new_grid[i][j + 1] = grid[i][j]

        grid = new_grid
        count += 1

    return grid
