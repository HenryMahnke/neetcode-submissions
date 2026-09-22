# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_value = float('-inf')
        def dfs(cur): 
            nonlocal max_path_value
            if cur is None: 
                return 0 
            left = max(0, dfs(cur.left))
            right = max(0,dfs(cur.right))
            max_path_value = max(max_path_value,left + cur.val + right)
            return cur.val + max(left,right)
        dfs(root)
        return max_path_value
        
