class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        for L in product(['|', '.'], repeat = len(s) - 1):
            subAns = []
            tmpStr = ""
            for i in range(len(s)):
                tmpStr += s[i]
                if i == len(s) - 1 or L[i] == '|':
                    subAns.append(tmpStr)
                    tmpStr = ""
            
            if all(t == t[::-1] for t in subAns):
                ans.append(subAns)
        
        return ans