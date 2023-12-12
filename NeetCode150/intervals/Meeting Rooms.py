class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        cnt = 0
        now = 0
        intervals.sort(key=lambda x: x[1])

        for i in range(n):
            if now <= intervals[i][0]:
                cnt += 1
                now = intervals[i][1]
                
        return cnt == n