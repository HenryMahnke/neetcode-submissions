# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#the way that this could be implemented is by recreating the inorder, and preorder reconstruction 
# and making those representations, otherwise 
import json
from queue import Queue

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        if root is None: 
            return ""
        arr.append(root.val)
        def bfs(node): 
            nonlocal arr
            frontier = Queue()
            frontier.put(root)
            while not frontier.empty():
                node = frontier.get()
                if node is not None:
                    if node.left: 
                        arr.append(node.left.val)
                    else: 
                        arr.append(None)
                    if node.right: 
                        arr.append(node.right.val)
                    else: 
                        arr.append(None)
                    if node.left:
                        frontier.put(node.left)
                    if node.right:
                        frontier.put(node.right)
                else: 
                    arr.append(None)
        bfs(root)
        return json.dumps(arr)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": 
            return None
        arr = json.loads(data) 
        frontier = Queue()
        root = TreeNode(arr[0],None,None)
        arr.pop(0)
        frontier.put(root)
        while frontier.empty() is False: 
            node = frontier.get() 
            if arr[0] is not None:
                node.left = TreeNode(arr[0],None,None)
                frontier.put(node.left)
            arr.pop(0)

            if arr[0] is not None:
                node.right = TreeNode(arr[0],None,None)
                frontier.put(node.right)
            arr.pop(0)
        return root



