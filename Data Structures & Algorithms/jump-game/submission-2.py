sys.setrecursionlimit(10000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hashmap = {}
        n = len(nums)


        def helper(i):
            if i in hashmap:
                return hashmap[i]
            if i == n-1:
                return True
            
            
            jump = nums[i]
            for j in range(1, jump+1):
                if helper(i+j):
                    hashmap[i+j] = True
                    return True
            hashmap[i] = False
            return False
        return helper(0)