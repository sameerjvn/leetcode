# leetcode 206
# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # time complexity : O(n)
        # space complexity: O(1)
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev 
        


    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        # time complexity : O(n)
        # space complexity: O(n)
        
        if not head:
            return None
        
        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
    
        return new_head