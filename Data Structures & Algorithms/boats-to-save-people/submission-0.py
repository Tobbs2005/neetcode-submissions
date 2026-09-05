class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0
        r = n-1
        res = 0
        while l <= r:
            if people[l] + people[r] > limit:
                r -= 1
                res += 1             
            else:
                r -= 1
                res += 1
                l += 1
        return res

        # 1 2 2 3 3