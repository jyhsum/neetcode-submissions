# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        
        removeIdx = count - n
        if removeIdx == 0:
            return head.next
        
        cur = head
        for i in range(count):
            if i + 1 == removeIdx:
                cur.next = cur.next.next
                break
            cur = cur.next
        
        return head
