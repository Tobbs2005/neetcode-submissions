"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    map = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # recursive solution
        if not head:
            return None
        if head in self.map:
            return self.map[head]
        cpy = Node(head.val)
        self.map[head] = cpy

        cpy.next = self.copyRandomList(head.next)

        cpy.random = self.map.get(head.random)
        return cpy