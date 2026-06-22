class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find index of pivot

        l = 0
        r = len(nums)-1
        
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        if target <= nums[-1]:
            #search from m to end
            l = l
            r = len(nums)-1
        else:
            r = l
            l = 0
        
        while l < r:                    
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:  
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1