class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        curr = []
        res = []
        n = len(nums)
        def backtrack(curr, i):
            
            if i >= n:
                res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(curr, i+1)
            curr.remove(nums[i])
            backtrack(curr, i+1)
        backtrack([], 0)
        return res

