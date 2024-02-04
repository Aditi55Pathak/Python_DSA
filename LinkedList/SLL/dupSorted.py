class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        if curr is None:
            return 
        nxt = curr.next
        
        while curr.next is not None:
            if nxt is not None and curr.val == nxt.val:
                curr.next = nxt.next
                nxt = nxt.next
            else:
                curr = curr.next
                if nxt is not None:
                    nxt = nxt.next
               
        return head
