class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        n = len(nums)
        res = 0
        total = 0
        for i, num in enumerate(nums):
            total += num
            need = total - k
            res += hashmap[need]
            hashmap[total] += 1
        return res

            