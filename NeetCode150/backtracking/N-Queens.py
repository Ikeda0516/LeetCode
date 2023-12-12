class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        seenCol = set()
        seenDiag1 = set() # i + j
        seenDiag2 = set() # i - j
        board = [['.'] * n for _ in range(n)]
        ans = []

        def dfs(i):
            if n == i:
                subAns = ["".join(b) for b in board]
                ans.append(subAns)
                return
            
            for j in range(n):
                if (j in seenCol) or (i + j in seenDiag1) or (i - j in seenDiag2):
                    continue

                seenCol.add(j)
                seenDiag1.add(i + j)
                seenDiag2.add(i - j)
                board[i][j] = 'Q'

                dfs(i + 1)

                seenCol.remove(j)
                seenDiag1.remove(i + j)
                seenDiag2.remove(i - j)
                board[i][j] = '.'
        
        dfs(0)
        return ans