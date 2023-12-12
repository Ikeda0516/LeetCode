class unionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cost(i, j):
            costx = abs(points[i][0] - points[j][0])
            costy = abs(points[i][1] - points[j][1])
            return costx + costy
        
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((i, j, cost(i, j)))
        edges.sort(key = lambda x: x[2])

        uf = unionFind(len(points))
        ans = 0
        for k in range(len(edges)):
            point1 = uf.find(edges[k][0])
            point2 = uf.find(edges[k][1])
            if point1 != point2:
                uf.union(point1, point2)
                ans += edges[k][2]
        
        return ans