# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using slow fast pointer also called floyd's approach
        # its just nothing placing at beginnning and looping through entire ll and if we
        # find slow == fast we will just say there is a linkedlist
        # this is called Cycle Detection
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        