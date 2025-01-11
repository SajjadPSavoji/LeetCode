# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

from collections import deque
from typing import List

class Solution:
    def dfs(self, i: int) -> None:
        # Cache frequently used variables locally
        isConnected = self.isConnected
        visited = self.visited
        
        visited[i] = True
        stack = [i]
        while stack:
            cur = stack.pop()
            # Instead of enumerate, using range() to access indices
            for j in range(len(isConnected[cur])):
                if isConnected[cur][j] and not visited[j]:
                    visited[j] = True
                    stack.append(j)
    
    def bfs(self, i: int) -> None:
        isConnected = self.isConnected
        visited = self.visited
        
        visited[i] = True
        queue = deque([i])
        while queue:
            cur = queue.popleft()
            for j in range(len(isConnected[cur])):
                if isConnected[cur][j] and not visited[j]:
                    visited[j] = True
                    queue.append(j)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # Use booleans for clarity and efficiency
        self.visited = [False] * n
        self.isConnected = isConnected
        groups = 0
        
        for i in range(n):
            if not self.visited[i]:
                groups += 1
                # You can choose either DFS or BFS for traversal:
                # self.bfs(i)  # Uncomment to use BFS
                self.dfs(i)  # Uncomment to use DFS
                
        return groups
