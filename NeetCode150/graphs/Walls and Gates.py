lass Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        m = len(rooms)
        n = len(rooms[0])

        adj = [[] for _ in range(m * n)]
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                for di, dj in move:
                    ii = i + di; jj = j + dj
                    if not (0 <= ii < m and 0 <= jj < n): continue
                    if rooms[i][j] == -1 or rooms[ii][jj] == -1: continue
                    adj[i * n + j].append(ii * n + jj)

        dist = [-1] * (m * n)
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dist[i * n + j] = 0
                    queue.append(i * n + j)
        
        while queue:
            frm = queue.popleft()
            for to in adj[frm]:
                if dist[to] == -1:
                    dist[to] = dist[frm] + 1
                    queue.append(to)

        for i in range(m):
            for j in range(n):
                if dist[i * n + j] != -1:
                    rooms[i][j] = dist[i * n + j] 