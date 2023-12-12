class Solution:
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        n = len(strs)

        for i in range(n):
            sortedWord = "".join(sorted(strs[i]))
            dic[sortedWord].append(strs[i])
        
        return dic.values()