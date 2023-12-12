class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = [0]
        intervals.sort()

        for start, end in intervals:
            if start < ans[0]:
                heappush(ans, end)
            else:
                heapreplace(ans, end)
        
        return len(ans)