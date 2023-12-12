class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        Lmul = [1] * (N + 1)
        Rmul = [1] * (N + 1)

        for i in range(N):
            Lmul[i + 1] = Lmul[i] * nums[i]
        for i in range(N):
            Rmul[~(i + 1)] = Rmul[~i] * nums[~i]

        ans = [0] * N
        for i in range(N):
            ans[i] = Lmul[i] * Rmul[i + 1]
        
        return ans