# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # we can recursively do this by flipping the first k nodes then call on the next ones
        if k == 1:
            return head
        #base case
        count = 1
        curr = head
        while curr:
            count += 1
            curr = curr.next
            if count == k:
                break
        
        if count < k or not curr:
            return head
    
        red = curr.next


        prev = red
        curr = head
        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = self.reverseKGroup(red, k)
        return prev




