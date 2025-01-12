# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows:
            return -1
        cols = len(grid[0])
        
        fresh_cnt = 0
        rotten = deque()
        
        # Preload the rotten oranges and count the fresh ones
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == 2:
                    rotten.append((r, c))
                elif cell == 1:
                    fresh_cnt += 1
        
        minutes_passed = 0
        # Predefine the four possible directions
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        
        while rotten and fresh_cnt:
            minutes_passed += 1
            # Process all rotten oranges in current minute
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    xx, yy = x + dx, y + dy
                    # Continue if out of bounds or not a fresh orange
                    if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        fresh_cnt -= 1
                        rotten.append((xx, yy))
                        
        return minutes_passed if fresh_cnt == 0 else -1
