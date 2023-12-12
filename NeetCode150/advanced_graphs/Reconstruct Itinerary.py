class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		adj = defaultdict(list)
		for frm, to in tickets:
			heappush(adj[frm], to)
		ans = []

		def topologicalSort(frm):
			while adj[frm]:
				to = heappop(adj[frm])
				topologicalSort(to)
			ans.append(frm)
		
		topologicalSort("JFK")
		return ans[::-1]