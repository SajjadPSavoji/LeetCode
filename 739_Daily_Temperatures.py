# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n  # Faster initialization
        stack = []
        
        # Assign methods and variables to local names for faster access
        append = stack.append
        pop = stack.pop
        temp = temperatures
        
        for i in range(n):
            current_temp = temp[i]
            # Resolve all indices in the stack that have a lower temperature
            while stack and temp[stack[-1]] < current_temp:
                j = pop()
                answer[j] = i - j
            append(i)
        
        return answer
