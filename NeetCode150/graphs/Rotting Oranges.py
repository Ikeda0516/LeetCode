class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        cnt = [0] * 3
        for i in range(m):
            for j in range(n):
                cnt[grid[i][j]] += 1
        if cnt[1] == 0:
            return 0
        elif cnt[2] == 0 and cnt[1] > 0:
            return -1

        adj = [[] for _ in range(m * n)]
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(m):
            for j in range(n):
                for di, dj in move:
                    ii, jj = i + di, j + dj
                    if not (0 <= ii < m and 0<= jj < n):
                        continue 
                    if grid[i][j] != 0 and grid[ii][jj] != 0:
                        adj[i * n + j].append(ii * n + jj)

        dist = [-1] * (m * n)
        Q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dist[i * n + j] = 0
                    Q.append(i * n + j)
        while Q:
            frm = Q.popleft()
            for to in adj[frm]:
                if dist[to] == -1:
                    dist[to] = dist[frm] + 1
                    Q.append(to)
      
        seen = [False] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or dist[i * n + j] != -1:
                    seen[i * n + j] = True

        return max(dist) if all(seen) else -1