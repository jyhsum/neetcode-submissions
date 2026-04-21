# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        q = deque([root])

        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    tmp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if tmp:
                res.append(tmp)
        
        return res