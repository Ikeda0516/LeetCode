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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for a, b in edges:
            A = uf.find(a)
            B = uf.find(b)
            if A == B:
                return False
            uf.union(A, B)

        for i in range(n):
            uf.find(i)
            
        return len(set(uf.p)) == 1