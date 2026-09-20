# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            leftHeight = 1
            rightHeight =1
            if root.left:
                leftHeight = 1 + dfs(root.left) 
            if root.right:
                rightHeight = 1 + dfs(root.right)
            # print(leftHeight, rightHeight)
            return max(leftHeight,rightHeight)
        if root:
            return dfs(root)
        else:
            return 0