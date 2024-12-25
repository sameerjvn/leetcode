# leetcode 19
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # iteration (two pass)
        # time complexity: O(n)
        # space complexity: O(1)


        # start with dummy node so that single element case can be handled
        new_head = ListNode()
        new_head.next = head

        # count number of nodes
        num_nodes = 0
        node = new_head
        while node:
            num_nodes += 1
            node = node.next
            
        # go to node before required node
        num_jumps = num_nodes - n - 1
        node = new_head
        for _ in range(num_jumps):
            node = node.next

        # point it to the node after next and remove the unwanted node from the list
        tmp = node.next
        node.next = node.next.next
        tmp.next = None

        return new_head.next