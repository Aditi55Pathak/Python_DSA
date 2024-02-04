# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_node = ListNode()
        temp1, temp2, temp3 = l1, l2, new_node

        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:
                temp3.next = temp1
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp2 = temp2.next
            temp3 = temp3.next

        # Check if there are remaining nodes in l1 or l2
        if temp1 is not None:
            temp3.next = temp1
        if temp2 is not None:
            temp3.next = temp2

        return new_node.next  # Return the head of the merged list

# Example usage:
# Create instances of ListNode and Solution
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()

# Call the mergeTwoLists method
merged_list = solution.mergeTwoLists(list1, list2)
print(merged_list)  # This will print the merged list
