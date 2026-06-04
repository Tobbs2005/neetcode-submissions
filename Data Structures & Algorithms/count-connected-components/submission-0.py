class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adj
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        seen = set()
        def dfs(curr):
            if curr in seen:
                return
            seen.add(curr)
            for n in adj[curr]:
                dfs(n)
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans

            

        