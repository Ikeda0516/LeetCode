class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        cur = head
        for _ in range(k):
            if not cur: return head
            cur = cur.next
        
        cur = head
        prev = None
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        head.next = self.reverseKGroup(cur, k)
        return prev