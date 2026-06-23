class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        search = self.storage[key]
        # we have a list of tuples
        #[("a", 1), ("b", 2)]
        # binary search
        l = 0
        r = len(search)

        while l < r:
            m = (l+r)//2
            if search[m][1] > timestamp:
                r = m
            else:
                l = m+1
        return search[l-1][0] if l > 0 else ""

