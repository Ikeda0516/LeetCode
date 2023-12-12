class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={None:None}
        cur=head
        while cur:
            dic[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy=dic[cur]
            copy.next=dic[cur.next]
            copy.random=dic[cur.random]
            cur=cur.next
        return dic[head]