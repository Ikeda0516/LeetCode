class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 10 ** 20
        adj = [[] for _ in range(n)]
        for frm, to, time in times:
            adj[frm - 1].append((time, to - 1))
        
        seen = [False] * n
        dist = [INF] * n
        dist[k - 1] = 0
        hq = []
        heappush(hq, (0, k - 1))
        while hq:
            frmTime, frm = heappop(hq)
            if seen[frm]: continue
            seen[frm] = True
            for toTime, to in adj[frm]:
                if dist[to] > frmTime + toTime:
                    dist[to] = frmTime + toTime
                    heappush(hq, (dist[to], to))
        
        ans = max(dist)
        return ans if ans != INF else -1