class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[-1]*n for _ in range(m)]
        queue=[(grid[0][0],0,0)]
        heapq.heapify(queue)
        vis[0][0] = 0
        while queue:
            mx,x,y=heapq.heappop(queue)
            if x==m-1 and y==n-1:
                return mx
            row=[0,0,-1,1]
            col=[1,-1,0,0]
            for i in range(4):
                if 0<=x+row[i]<m and 0<=y+col[i]<n:
                    if vis[x+row[i]][y+col[i]] == -1:
                        heapq.heappush(queue,(max(mx,grid[x+row[i]][y+col[i]]),x+row[i],y+col[i]))
                        vis[x+row[i]][y+col[i]] = 1