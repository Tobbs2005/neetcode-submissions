class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # flip the index
        n = len(nums)
        for i in range(n):
            curr = abs(nums[i])
            if nums[curr] < 0:
                return curr
            # flip to indicate seen
            nums[curr] *= -1

