class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1] - x[0])
        sortedQueries = sorted([val, i] for i, val in enumerate(queries))
        res = [-1] * len(queries)
        
        for left, right in intervals:
            i = bisect_left(sortedQueries, [left])
            while i < len(sortedQueries) and sortedQueries[i][0] <= right:
                res[sortedQueries.pop(i)[1]] = right - left + 1
        
        return res