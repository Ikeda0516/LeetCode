class UnionFind:
    def __init__(self,n):
        self.p=list(range(n))
        self.r=[0]*n
    def find(self,x):
        if self.p[x]!=x: self.p[x]=self.find(self.p[x])
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for a, b in edges:
            if uf.find(a - 1) == uf.find(b - 1):
                return [a, b]
            else:
                uf.union(a - 1, b - 1)