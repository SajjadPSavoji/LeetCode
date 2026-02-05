# 465. Optimal Account Balancing
# Solved
# Hard

# Topics
# conpanies icon
# Companies
# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

# Return the minimum number of transactions required to settle the debt.

 

# Example 1:

# Input: transactions = [[0,1,10],[2,0,5]]
# Output: 2
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
# Example 2:

# Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
# Output: 1
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

# Constraints:

# 1 <= transactions.length <= 8
# transactions[i].length == 3
# 0 <= fromi, toi < 12
# fromi != toi
# 1 <= amounti <= 100

from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # 1) Net balance per person
        bal = defaultdict(int)
        for f, t, amt in transactions:
            bal[f] -= amt
            bal[t] += amt

        # 2) Keep only non-zero balances
        debt = [v for v in bal.values() if v != 0]
        n = len(debt)
        if n == 0:
            return 0

        # 3) DFS: settle debt[start] by pairing with opposite sign
        def dfs(start: int) -> int:
            # skip already-settled people
            while start < n and debt[start] == 0:
                start += 1
            if start == n:
                return 0

            best = float("inf")
            seen = set()  # prune: don't try same debt[j] value twice at this level

            for j in range(start + 1, n):
                if debt[j] == 0:
                    continue
                # must be opposite signs to cancel
                if debt[start] * debt[j] >= 0:
                    continue
                if debt[j] in seen:
                    continue
                seen.add(debt[j])

                # try settling start with j (one transaction)
                orig_j = debt[j]
                debt[j] += debt[start]

                best = min(best, 1 + dfs(start + 1))

                # backtrack
                debt[j] = orig_j

                # perfect cancel prune: if this made j exactly 0, no need to try other j's
                if debt[j] + debt[start] == 0:
                    break

            return best

        return dfs(0)
