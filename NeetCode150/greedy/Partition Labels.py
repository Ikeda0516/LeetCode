class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last ={char: i for i, char in enumerate(S)}
        left, right = 0, 0
        ans = []

        for i, char in enumerate(S):
            right = max(right, last[char])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        
        return ans