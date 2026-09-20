# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # get map of inorder map indexes to do conversion 
        inorder_map = {}
        # takes in preorder VALUE not INDEX
        for j in range(len(inorder)):
            inorder_map[inorder[j]] = j
        i = 0
        def f(l,r): 
            nonlocal i
            nonlocal inorder_map
            root_val = preorder[i]
            root = TreeNode(root_val,None,None)
            if r - l == 1: 
                i+=1
                return root
            inorder_ind = inorder_map[root_val]
            i = i+1
            if inorder_ind - l > 0:
                root.left = f(l,inorder_ind)
            if r - (inorder_ind+1) > 0:
                root.right = f(inorder_ind+1, r)
            return root
        root = f(0,len(inorder))
        return root
