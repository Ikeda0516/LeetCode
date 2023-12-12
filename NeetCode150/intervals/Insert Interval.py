class Solution:
    def insert(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[1]
        left, right = [], []

        for interval in intervals:
            if interval[1] < s:
                left.append(interval)
            elif e < interval[0]:
                right.append(interval)
            else:
                s = min(s, interval[0])
                e = max(e, interval[1])
                
        return left + [[s, e]] + right