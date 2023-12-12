class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        for L in product(range(2), repeat = 2 * n):
            stack = []
            tmp = ""
            valid = True
            for i in range(len(L)):
                if L[i] == 0:
                    tmp += '('
                    stack.append('(')
                else:
                    tmp += ')'
                    if stack:
                        stack.pop()
                    else:
                        valid = False
            if not stack and valid:
                print(tmp)
                ans.append(tmp)
        
        return ans