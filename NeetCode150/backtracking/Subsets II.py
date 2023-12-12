class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for tpl in product(range(2), repeat = len(nums)):
            subAns = []
            for i in range(len(tpl)):
                if tpl[i] == 1:
                    subAns.append(nums[i])
            subAns.sort()
            if subAns not in ans:
                ans.append(subAns)
        
        return ans