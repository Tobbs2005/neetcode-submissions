# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use a queue
        queue = []
        output = []
        if not root:
            return []
        queue.append(root)
        while queue:
            level = len(queue)
            curr = []
            for i in range(level):
                node = queue[0]
                curr.append(node.val)
                if node.left:
                    queue.append(queue[0].left)
                if node.right:
                    queue.append(queue[0].right)
                del queue[0]
            output.append(curr)
            level = level * 2
        return output
