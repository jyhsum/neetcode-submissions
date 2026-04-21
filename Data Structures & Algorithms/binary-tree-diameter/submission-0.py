# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)} # 當節點為None直接給他預設值0

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)  #檢查當前node有沒有child, 有的畫append child這樣下次處理的就會是child
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]
                mp[node] = (1 + max(leftHeight, rightHeight),
                            max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]