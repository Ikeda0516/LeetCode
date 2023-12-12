class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]
        def bfs(q):
            visited = set()
            q = collections.deque(q)
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for ii, jj in map(lambda x: (x[0]+i, x[1]+j), [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in visited and matrix[ii][jj] >= matrix[i][j]:
                        q.append((ii, jj))
            return visited     
        return bfs(pacific) & bfs(atlantic)