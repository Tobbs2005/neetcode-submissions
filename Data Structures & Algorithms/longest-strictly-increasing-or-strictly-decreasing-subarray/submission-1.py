class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        n = len(nums)
        ans = 0
        if len(nums) <= 1:
            return len(nums)
        while r < n-1:
            
            print(l, r)
            if nums[r] < nums[r+1]:
                #strinctly increasing
                r += 1
            else:
                l = r + 1
                r += 1
            ans = max(ans, r-l + 1)

        l = 0 
        r = 0
        while r < n-1:
            
            if nums[r] > nums[r+1]:
                #strinctly decreasing
                r += 1
            else:
                l = r + 1
                r += 1
            ans = max(ans, r-l + 1)

        return ans