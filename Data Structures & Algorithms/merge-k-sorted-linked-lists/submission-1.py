# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        head = ListNode()
        heap = []
        tie = 0
        for i in range(k):
            tie += 1
            curr = lists[i]
            heapq.heappush(heap, [curr.val, tie, curr])

        # heap [value, pointer]
        walk = head
        while heap:

            tie += 1
            val, _, curr = heapq.heappop(heap)
            node = ListNode(val)
            walk.next = node
            walk = walk.next
            if curr.next:
                heapq.heappush(heap, [curr.next.val, tie, curr.next])
        return head.next
            


