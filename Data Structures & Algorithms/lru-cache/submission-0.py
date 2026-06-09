class LRUCache:
    # we can use a hashmap to store a node
    # move node so head is most recent, tail is least
    class Node:
        def __init__(self, key, value):
            self.next = None
            self.prev = None
            self.val = value
            self.key = key


    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cap = capacity
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0




    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.updateRecent(key)
        
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:          # update existing node
            self.hashmap[key].val = value
            self.updateRecent(key)
            return
        if self.size >= self.cap:
            # remove LRU 
            self.removeLRU()
            self.size -= 1
        self.size += 1
        node = self.Node(key, value)
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.hashmap[key] = node
        
    def removeLRU(self):
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        del self.hashmap[last.key]

    def updateRecent(self, recent):
        node = self.hashmap[recent]
        head = self.head 
        tail = self.tail
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = head.next
        head.next.prev = node
        head.next = node
        node.prev = head

    
    
        
