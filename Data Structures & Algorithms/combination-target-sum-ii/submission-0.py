class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def recursion(curr_list, curr_sum, index):
            if curr_sum == target:
                ans.append(curr_list[:])
                return
            
            if(curr_sum > target or index == len(candidates)):
                return
            prev = -1
            for i in range(index, len(candidates)):
                if(prev == candidates[i]): 
                    continue
                prev = candidates[i]
                curr_sum += candidates[i]
                curr_list.append(candidates[i])
                recursion(curr_list, curr_sum, i+1)
                curr_sum -= candidates[i]
                curr_list.pop()

        recursion([], 0, 0)
        return ans
        


