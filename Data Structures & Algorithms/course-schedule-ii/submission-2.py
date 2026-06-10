class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for prereq in prerequisites:
            pre[prereq[0]].append(prereq[1])
        
        ans = []
        seen = set()
        done = set()
        def dfs(curr):
            if curr in seen:
                return False
            if curr in done:       # ← already processed, skip
                return True
            seen.add(curr)
            for r in pre[curr]:
                if not dfs(r):
                    return False
            pre[curr] = []
            seen.remove(curr)
            done.add(curr)
            ans.append(curr)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return ans
        