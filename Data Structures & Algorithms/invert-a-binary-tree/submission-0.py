# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            if not node:
                return
            l = helper(node.left)
            r = helper(node.right)
            
            node.left = r
            node.right = l
            return node
        
        helper(root)
        return root




        