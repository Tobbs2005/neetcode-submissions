class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def getDistance(a, b):
            return abs(a-b)
        
        curr = 0
        n = len(arr)
        while curr < n and arr[curr] < x:
            curr += 1
        
        l = curr-1
        r = curr
        res = []
        for _ in range(k):
            if l < 0:
                res.append(arr[r])
                r += 1
                continue
            elif r >= n:
                res.append(arr[l])
                l -= 1
                continue

            if getDistance(x, arr[l]) <= getDistance(x, arr[r]):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return sorted(res)

        
        