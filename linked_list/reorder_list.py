# leetcode 143
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # time complexity: O(n)
        # space complexity: O(1)

        # find midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split
        second = slow.next
        slow.next = None
        
        # reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two linked lists alternatively
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 