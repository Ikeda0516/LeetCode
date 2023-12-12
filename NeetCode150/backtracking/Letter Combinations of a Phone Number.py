class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = []
        letter = ["abc.", "def.", "ghi.", "jkl.", "mno.", "pqrs", "tuv.", "wxyz"]

        for L in product(range(4), repeat = len(digits)):
            subAns = ""
            for i in range(len(L)):
                subAns += letter[int(digits[i]) - 2][L[i]]
            if '.' not in subAns:
                ans.append(subAns)
        
        return ans