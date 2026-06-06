class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #monotonic decreasing queue
        queue = deque()

        
            
        def queueadd(x, queue):
            if len(queue) == 0:
                queue.append(x)
                return
            
            while len(queue) != 0 and queue[len(queue)-1] < x:
                queue.pop()

            queue.append(x)

        for r in range(k):
            queueadd(nums[r], queue)
            

        l = 0
        n = len(nums)
        ans = [queue[0]]

    
        
        while r < n-1:
  
            r += 1
            if queue[0] == nums[l]:
                queue.popleft()
            queueadd(nums[r], queue)
            ans.append(queue[0])
            l += 1
        return ans
