# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,min_val, max_val): 
            print("min_val", min_val, "max_val", max_val)
            print(root.val)
            val1 = True 
            val2 = True
            if root.left: 
                val1 = dfs(root.left, min_val, root.val) 
            if root.right: 
                val2 = dfs(root.right, root.val, max_val) 
            if root.val <= min_val or root.val >= max_val: 
                return False
            print(val1, val2)
            return val1 and val2
        return dfs(root, -float('inf'), float('inf'))
