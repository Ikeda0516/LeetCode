class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(arr, trg, path):
            if trg == 0:
                ans.append(path)
                return
            for i in range(len(arr)):
                if i - 1 >= 0 and arr[i - 1] == arr[i]: continue
                if arr[i] > trg: break
                dfs(arr[i + 1:], trg - arr[i], path + [arr[i]])
        
        ans = []
        dfs(sorted(candidates), target, [])
        return ans