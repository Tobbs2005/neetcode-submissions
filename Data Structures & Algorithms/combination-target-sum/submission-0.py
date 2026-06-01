class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def recursion(curr_list, curr_sum, index):
            if curr_sum == target:
                ans.append(curr_list[:])
                return
            
            if(curr_sum > target):
                return
            
            for i in range(index, len(nums)):
                curr_sum += nums[i]
                curr_list.append(nums[i])
                recursion(curr_list, curr_sum, i)
                curr_sum -= nums[i]
                curr_list.pop()

        recursion([], 0, 0)
        return ans
        


