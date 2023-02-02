"""
Given the head of a sorted linked list, delete all duplicates such that each 
element appears only once. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        head_to_ret = head
        
        while head.next != None:
            tmp_val = head.val
            tmp_next = head.next
            if tmp_val == tmp_next.val:
                head.next = tmp_next.next
            else:
                head = head.next
        return head_to_ret


