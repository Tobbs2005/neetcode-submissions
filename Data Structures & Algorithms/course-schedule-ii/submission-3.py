class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological answer
        premap = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        for req in prerequisites:
            premap[req[1]].append(req[0])
            indegree[req[0]] += 1

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0, []
        while q:
            node = q.popleft()
            output.append(node)
            finish += 1
            for nei in premap[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        return output
