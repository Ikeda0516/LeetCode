class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=""
        num2=""

        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next

        total = str(int((num1)[::-1]) + int((num2)[::-1]))[::-1]
        dummy=ListNode(0)
        cur=dummy
        for i in total:
            cur.next=ListNode(int(i))
            cur=cur.next

        return dummy.next