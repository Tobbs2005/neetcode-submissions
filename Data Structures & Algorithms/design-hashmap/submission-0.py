
        
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        # our hash will be 1000
        self.hashset = [ListNode(-1, -1) for i in range(1000)]


    def put(self, key: int, value:int) -> None:
        hashed = key % 1000
        head = self.hashset[hashed]

        node = head.next
        prev = head
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
            prev = prev.next
        prev.next = ListNode(key, value)
        

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
                
        
        

    def get(self, key: int) -> int:
        hashed = key % 1000
        head = self.hashset[hashed]
        node = head.next
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)