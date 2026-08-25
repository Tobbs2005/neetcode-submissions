class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        offset = 0

        for i in range(n):
            print(nums)
            print(offset)
            temp = i
            while i + offset < n and nums[i + offset] == val:
                offset += 1
                temp += 1
            if i+offset >= n:
                return n-offset
            nums[i] = nums[i+offset]
            
        return n-offset

 
