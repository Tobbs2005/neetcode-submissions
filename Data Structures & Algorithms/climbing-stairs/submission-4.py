import functools
class Solution:
    hashmap = {}
    def climbStairs(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.hashmap[n] = ans
        return ans