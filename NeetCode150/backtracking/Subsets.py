class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for tpl in product(range(2), repeat = len(nums)):
            subAns = []
            for i in range(len(tpl)):
                if tpl[i] == 1:
                    subAns.append(nums[i])
            ans.append(subAns)
        
        return ans