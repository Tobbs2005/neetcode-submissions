# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find midpoint
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #split at slow and reverse the end
        second = slow.next
        slow.next = None


        reverse = self.reverseList(second)


        #now merge
        while head and reverse:
            temp = reverse.next
            reverse.next = head.next
            head.next = reverse
            reverse = temp
            head = head.next.next
        
        #if theres remaining add it

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
