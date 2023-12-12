class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(board, i, j, cnt):
            if(cnt == len(word)):
                return True
            if not (0 <= i < rows and 0 <= j < cols) or word[cnt] != board[i][j]:
                return False

            tmp = board[i][j]
            board[i][j] = ""
            up_dfs = dfs(board, i + 1, j, cnt + 1)
            down_dfs = dfs(board, i - 1, j, cnt + 1)
            right_dfs = dfs(board, i, j + 1, cnt + 1)
            left_dfs = dfs(board, i, j - 1, cnt + 1)
            seen = up_dfs or down_dfs or right_dfs or left_dfs
            board[i][j] = tmp

            return seen
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(board, i, j, 0):
                    return True
        return False