# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l1_str = ""
        l2_str = ""

        while l1:
            l1_str += str(l1.val)
            l1 = l1.next
        
        while l2:
            l2_str += str(l2.val)
            l2 = l2.next

        result_str = str(int(l1_str[::-1]) + int(l2_str[::-1]))
        result = []
        for num in result_str:
            result.append(int(num))
        result.reverse()
        
        dummy = ListNode()
        curr = dummy

        for num in result:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next




    

        