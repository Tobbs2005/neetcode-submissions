# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we can keep a front and a back pointer
        front = head
        back = head
        previous = None
        for i in range(n):
            front = front.next
        
        while front:
            previous = back
            front = front.next
            back = back.next
        if not previous:
            return head.next
        previous.next = back.next
        return head
        