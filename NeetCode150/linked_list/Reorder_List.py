class Solution:
    def reorderList(self, head):
        if not head:
            return head
    
        dummy = ListNode()
        dummy.next = head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        second = slow.next
        slow.next = None
    
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
    
        second = prev
    
        while head and second:
            node1 = head.next
            node2 = second.next
            head.next = second
            second.next = node1
            head = node1
            second = node2
    
        return dummy.next