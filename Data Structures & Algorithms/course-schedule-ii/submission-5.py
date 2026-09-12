class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for c, p in prerequisites:
            indegree[c] += 1
            adj[p].append(c)

        # topological

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        

        count = 0
        res = []

        while queue:

            curr = queue.popleft()
            count += 1
            res.append(curr)

            for neighbour in adj[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
           
        return res if len(res) == numCourses else []


        


