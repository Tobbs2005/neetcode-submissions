class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        curr = []
        def backtrack(i):
            if len(curr) == len(nums) or i >= len(nums):
                ans.append(curr.copy())
                return
            
            # add curr and increment
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

            # dont add
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return ans

