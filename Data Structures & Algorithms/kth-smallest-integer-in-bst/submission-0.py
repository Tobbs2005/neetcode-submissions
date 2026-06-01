# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, count):
            if not node:
                return count, None
            count, left = dfs(node.left, count)
            if left:
                return count, left

            count += 1
            if count == k:
                return count, node.val
            
            return  dfs(node.right, count)
        _, res = dfs(root, 0)
        return res
          
