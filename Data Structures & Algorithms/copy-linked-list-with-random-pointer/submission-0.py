"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp = {None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            tmp[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = tmp[cur]
            copy.next = tmp[cur.next]
            copy.random = tmp[cur.random]
            cur = cur.next
        
        return tmp[head]