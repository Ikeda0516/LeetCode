class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(hq, (lists[i].val, i))
                lists[i] = lists[i].next
        
        dummy = cur = ListNode()
        while hq:
            val, i = heappop(hq)
            cur.next = ListNode(val)
            if lists[i]:
                heappush(hq, (lists[i].val, i))
                lists[i] = lists[i].next
            cur = cur.next
        
        return dummy.next