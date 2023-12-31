class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        while n:
            fast = fast.next
            n -= 1
        
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head