# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        new_list = ListNode(0)
        new_list_tail = new_list

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                new_list.next = curr1
                new_list = new_list.next
                curr1 = curr1.next
            else:
                new_list.next = curr2
                new_list = new_list.next
                curr2 = curr2.next
        
        while curr1:
            new_list.next = curr1
            new_list = new_list.next
            curr1 = curr1.next
        
        while curr2:
            new_list.next = curr2
            new_list = new_list.next
            curr2 = curr2.next
        
        return new_list_tail.next
            
