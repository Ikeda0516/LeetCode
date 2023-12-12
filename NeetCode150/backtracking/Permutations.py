class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for tpl in permutations(nums, len(nums)):
            ans.append(list(tpl))
            
        return ans