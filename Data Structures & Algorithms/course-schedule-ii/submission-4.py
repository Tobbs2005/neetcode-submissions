class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)

        seen = set()
        curr = set()

        res = []
        def dfs(course):
            if course in curr: 
                return False
            if course in seen:
                return True 
            curr.add(course)
            
            
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            curr.remove(course)
            seen.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            
            if not dfs(i):
                return []

        return res
