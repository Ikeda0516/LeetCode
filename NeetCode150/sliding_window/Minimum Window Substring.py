class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCnt, tCnt = Counter(), Counter(t)
        l = 0
        ans = "@" * (10 ** 6)

        for r in range(len(s)):
            sCnt[s[r]] += 1
            if sCnt & tCnt != tCnt:
                continue
            while l <= r:
                sCnt[s[l]] -= 1
                l += 1
                if sCnt & tCnt == tCnt:
                    continue
                if len(ans) > len(s[l - 1:r + 1]):
                    ans = s[l - 1:r + 1]
                break
        
        return ans if ans != "@" * (10 ** 6) else ""