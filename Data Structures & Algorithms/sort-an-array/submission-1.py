import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(a, b):
            if a == b:
                return
            i = a-1
            j = a
            r = random.randrange(a, b)                  
            nums[r], nums[b-1] = nums[b-1], nums[r]
            part = nums[b-1]
            while j < b-1:
                if nums[j] < part:
                    # swap 
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

                else:
                    j += 1
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

            partition(a, i)
            partition(i+1, b)

        n = len(nums)
        partition(0, n)
        return nums




        

        