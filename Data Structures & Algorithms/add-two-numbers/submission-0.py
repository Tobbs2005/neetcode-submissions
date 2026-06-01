# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # recursive

        carry = 0
        def add(l1, l2):
            nonlocal carry
            if not l1 and not l2 and carry == 0:
                return None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            value = v1+v2+carry
            if value > 9:
                carry = 1
                value = value%10
            else:
                carry = 0
            
                
            next_node = add(
                l1.next if l1 else None,
                l2.next if l2 else None
            )
            return ListNode(value, next_node)


        return add(l1,l2)


    