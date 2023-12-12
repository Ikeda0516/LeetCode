class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(arr, trg, path):
            if trg == 0:
                res.append(path)
                return
            for i in range(len(arr)):
                if arr[i] > trg:
                    continue
                dfs(arr[i:], trg - arr[i], path + [arr[i]])
        
        res = []
        dfs(candidates, target, [])
        return res