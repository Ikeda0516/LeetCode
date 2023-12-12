class UnionFind:
    def __init__(self,n):
        self.p=list(range(n))
        self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if self.r[x]>self.r[y]:
            self.p[y]=x
        else:
            self.p[x]=y
            if self.r[x]==self.r[y]:
                self.r[y]+=1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        uf = UnionFind(m * n)

        isExistOne = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    isExistOne = True
        if not isExistOne:
            return 0

        for i in range(m):
            for j in range(n):
                for di, dj in move:
                    ii = i + di
                    jj = j + dj
                    if not(0 <= ii < m and 0 <= jj < n): continue
                    if grid[i][j] == 0 or grid[ii][jj] == 0: continue
                    uf.union(i * n + j, ii * n + jj)
        
        for k in range(m * n):
            uf.find(k)
        
        cnt = Counter(uf.p)
        return cnt.most_common()[0][1]