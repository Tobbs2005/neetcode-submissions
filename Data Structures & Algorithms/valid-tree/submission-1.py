class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # cycle detection
        seen = set()
        def dfs(curr, prev):
            if curr in seen:
                return False
            seen.add(curr)
            for neighbor in adj[curr]:
                if neighbor == prev:   # skip the edge we just came from
                    continue
                if not dfs(neighbor, curr):
                    return False
            return True

        return dfs(0, -1) and len(seen) == n
        
        return dfs(0) and len(seen) == n