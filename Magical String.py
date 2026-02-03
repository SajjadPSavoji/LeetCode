# Q3. Magical String
# Solved
# Medium

# Topics
# premium lock icon
# Companies
# A magical string s consists of only '1' and '2' and obeys the following rule:

# Concatenating the sequence of lengths of its consecutive groups of identical characters '1' and '2' generates the string s itself.
# The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and counting the occurrences of 1's or 2's in each group yields the sequence "1 2 2 1 1 2 1 2 2 1 2 2 ......".

# You can see that concatenating the occurrence sequence gives us s itself.

# Given an integer n, return the number of 1's in the first n number in the magical string s.

 

# Example 1:

# Input: n = 6
# Output: 3
# Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 105

class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            # "122" -> first 1 has exactly one '1'
            return 1

        s = [1, 2, 2]
        ones = 1  # in "122", count of 1s is 1

        read = 2
        write = 3
        next_num = 1

        while write < n:
            run_len = s[read]
            read += 1

            # write next_num run_len times (but don't exceed n)
            for _ in range(run_len):
                if write >= n:
                    break
                s.append(next_num)
                if next_num == 1:
                    ones += 1
                write += 1

            # toggle between 1 and 2
            next_num = 2 if next_num == 1 else 1

        return ones
