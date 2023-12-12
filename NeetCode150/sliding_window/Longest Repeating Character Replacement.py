class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = l = 0
        cnt = Counter()
        ans = -1

        for r in range(len(s)):
            cnt[s[r]] += 1
            maxFreq = max(maxFreq, cnt[s[r]])
            if r - l + 1 > maxFreq + k:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans