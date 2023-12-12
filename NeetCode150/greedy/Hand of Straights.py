class Solution:
	def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
		if len(hand) % groupSize != 0:
			return False
		
		cnt = Counter(hand)
		keys = sorted(cnt.keys())
		for key in keys:
			val = cnt[key]
			if val == 0: continue
			for i in range(1, groupSize):
				if cnt[key + i] < val:
					return False
				cnt[key + i] -= val
		
		return True