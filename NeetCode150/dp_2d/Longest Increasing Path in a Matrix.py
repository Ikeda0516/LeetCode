class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dic = {}

        def dfs(i, j, parent):
            if not (0 <= i < rows and 0 <= j < cols) or matrix[i][j] <= parent: return 0
            if (i, j) in dic: return dic[(i, j)]

            res = 1
            res = max(res, dfs(i, j + 1, matrix[i][j]) + 1)
            res = max(res, dfs(i - 1, j, matrix[i][j]) + 1)
            res = max(res, dfs(i, j - 1, matrix[i][j]) + 1)
            res = max(res, dfs(i + 1, j, matrix[i][j]) + 1)
            dic[(i, j)] = res

            return res
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)
        
        return max(dic.values())