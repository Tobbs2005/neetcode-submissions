class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
  
        adj = defaultdict(list)


        def dfs(curr, prev):
            if curr in seen:
                return True
           
            seen.add(curr)
            for n in adj[curr]:
                if n == prev:
                    continue
                if dfs(n, curr):
                    return True
            
            return False
        for u, v in edges:
            adj[u].append(v)
            
            adj[v].append(u)
            seen = set()
            if dfs(u, -1):

                return [u,v]
        return []

