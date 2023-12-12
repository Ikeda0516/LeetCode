class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        seen = [False] * n
        adj = [[] for _ in range(n)]
        for frm, to in edges:
            adj[frm].append(to)
            adj[to].append(frm)

        def dfs(frm):
            if seen[frm]:
                return
            seen[frm] = True
            for to in adj[frm]:
                dfs(to)
        
        for i in range(n):
            if not seen[i]:
                dfs(i)
                ans += 1
        
        return ans