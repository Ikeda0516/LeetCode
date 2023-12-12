class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            adj[a].append(b)
            indeg[b] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)
        
        order = []
        while queue:
            frm = queue.popleft()
            order.append(frm)
            for to in adj[frm]:
                indeg[to] -= 1
                if indeg[to] == 0:
                    queue.append(to)
        
        if len(order) == numCourses:
            return order[::-1]
        else:
            return []