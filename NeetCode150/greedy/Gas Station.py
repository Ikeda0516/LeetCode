class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = [0] + list(accumulate([g - c for g, c in zip(gas, cost)]))
        return diff.index(min(diff)) if diff[-1] >= 0 else -1