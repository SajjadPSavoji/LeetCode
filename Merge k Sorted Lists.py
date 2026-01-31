# Q2. Merge k Sorted Lists
# Hard
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


import heapq
from typing import List, Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        heap = []
        counter = 0  # tie-breaker

        for head in lists:
            if head is not None:
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1

        while heap:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        cur.next = None  # optional: ensure tail ends cleanly
        return dummy.next
