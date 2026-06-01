class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        n = len(nums)
        picked = [False] * n
        def backtrack():
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            for i in range(len(nums)):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    backtrack()
                    curr.pop()
                    picked[i] = False
        backtrack()
        return ans

            