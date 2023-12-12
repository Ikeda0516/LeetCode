class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return

        s1Cnt = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            s2SubCnt = Counter(s2[i:i+len(s1)])
            if s1Cnt == s2SubCnt:
                return True
        return False