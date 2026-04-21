# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = set()

        while head:
            if head in l:
                return True
            else:
                l.add(head)
                head = head.next
        
        return False