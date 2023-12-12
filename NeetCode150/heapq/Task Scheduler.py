class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord('A')] += 1
        
        Max = max(cnt)
        maxCnt = 0
        for c in cnt:
            if c == Max:
                maxCnt += 1
        
        return max((Max - 1) * (n + 1) + maxCnt, len(tasks))