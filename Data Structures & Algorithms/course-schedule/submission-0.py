class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)
        for req in prerequisites:
            premap[req[0]].append(req[1])
        

        visiting = set()

        def dfs(curr):
            if curr in visiting:
                return False
            visiting.add(curr)
            for req in premap[curr]:
                if not dfs(req):
                    return False
            visiting.remove(curr)
            premap[curr] = []
            return True
        for c in range(numCourses):        # ← incomplete line
            if not dfs(c):
                return False
        return True
