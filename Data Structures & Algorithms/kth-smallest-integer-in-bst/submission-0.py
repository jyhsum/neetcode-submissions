# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dic = {}
        q = deque([root])

        while q:
            node = q.popleft()
            dic[node.val] = node

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        sorted_dic = dict(sorted(dic.items()))

        print(sorted_dic)
        
        count = 1
        for n in sorted_dic.keys():
            if count == k:
                return dic[n].val
            count += 1
