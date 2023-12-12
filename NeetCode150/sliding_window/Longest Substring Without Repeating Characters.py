class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        dic = defaultdict(int)

        for r in range(len(s)):
            if s[r] in dic:
                l = max(l, dic[s[r]] + 1)
            dic[s[r]] = r
            ans = max(ans, r - l + 1)
        
        return ans