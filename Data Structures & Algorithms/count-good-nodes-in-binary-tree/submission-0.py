# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node is good if path from root to tree node x contains no nodes with value greater than that of x
        count = 0
        def dfs(root, max_val):
            nonlocal count 
            if root.left: 
                dfs(root.left, max(max_val,root.val))
                # print("max_val",max(max_val, root.val))
            if root.right: 
                dfs(root.right,max(max_val,root.val))
                # print("max_val",max(max_val, root.val))
            if root.val >= max_val:
                count +=1
                # print("increasing count")
            # print("root:", root.val)
        
        dfs(root, root.val)
        return count