class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            elif len(hashmap) < 2:
                hashmap[num] = 1
            else: 
                for key in list(hashmap):
                    hashmap[key] -= 1
                    if hashmap[key] <= 0:
                        del hashmap[key]
  
      

            
        n = len(nums)
        res = []
        for key in hashmap:
            if nums.count(key) > n//3:
                res.append(key)

        return res

