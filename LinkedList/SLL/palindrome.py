class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        list_elem = []
        curr = head
        while curr:
            list_elem.append(curr.val)
            curr = curr.next

        list_elem_rev = list_elem[::-1]
        if list_elem == list_elem_rev:
            return True
        return False
