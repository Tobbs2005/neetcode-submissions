class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # two pointers
        # at no intersection, increment pointer with smaller end
        # at intersection, increment both pointers

        def isIntersect(a, b):
            return (a[1] >= b[0] and b[1] >= a[0])
                
        one = 0
        two = 0

        ans = []

        n = len(firstList)
        m = len(secondList)

        while one < n and two < m:
            a, b = firstList[one], secondList[two]
            lo = max(a[0], b[0])    
            hi = min(a[1], b[1])   
            if lo <= hi:           
                ans.append([lo, hi])
            
            # discrard smaller List
            if firstList[one][1] < secondList[two][1]:
                one += 1
            else:
                two += 1

        return ans
        
        