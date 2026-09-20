# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # assume k is less than the number of nodes in the tree 
        # can we get faster time complexity than an inorder traversal? 
        # no because we don't know the length of each tree from the ds
        # so, traverse inorder, easiest with recursion or iteration? 
        counter = 0
        cur = root
        counter = 0
        value = 0
        def recurse(cur: Optional[TreeNode]): 
            nonlocal counter
            nonlocal value
            nonlocal k
            if cur.left: 
                recurse(cur.left) 
            counter+=1
            if counter == k: 
                counter+=1
                value = cur.val
                return
            if cur.right: 
                recurse(cur.right) 
        recurse(root)
        return value


        