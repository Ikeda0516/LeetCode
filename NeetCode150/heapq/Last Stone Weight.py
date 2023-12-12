class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = [-s for s in stones]
        heapify(hq)

        while len(hq) >= 2:
            y = -heappop(hq)
            x = -heappop(hq)
            if x != y:
                heappush(hq, -(y - x))
        
        if not hq:
            return 0
        else:
            return -hq[0]