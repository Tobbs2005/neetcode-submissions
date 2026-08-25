class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        # our hash will be 1000
        self.hashset = [ListNode(-1) for i in range(1000)]


    def add(self, key: int) -> None:
        hashed = key % 1000
        head = self.hashset[hashed]

        node = head.next
        prev = head
        while node:
            if node.key == key:
                return
            node = node.next
            prev = prev.next
        prev.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        hashed = key % 1000
        head = self.hashset[hashed]
        node = head.next
        prev = head
        while node:
            if node.key == key:
                prev.next = node.next
            node = node.next
            prev = prev.next
                
        
        

    def contains(self, key: int) -> bool:
        hashed = key % 1000
        head = self.hashset[hashed]
        node = head.next
        while node:
            if node.key == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)