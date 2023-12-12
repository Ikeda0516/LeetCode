class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        total = int(num1[::-1]) + int(num2[::-1])
        dummy = ListNode()
        cur = dummy

        for t in str(total)[::-1]:
            cur.next = ListNode(int(t))
            cur = cur.next
        
        return dummy.next