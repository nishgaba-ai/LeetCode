# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        curr1 = l1
        curr2 = l2
        res = []
        while((curr1 is not None) and (curr2 is not None)):
            res.append((curr1.val+curr2.val+carry)%10)
            carry = (curr1.val+curr2.val+carry)/10
            curr1=curr1.next
            curr2=curr2.next
        if(curr1 is not None):
            while(curr1 is not None):
                res.append((curr1.val+carry)%10)
                carry = (curr1.val+carry)/10
                curr1=curr1.next
        elif(curr2 is not None):
            while(curr2 is not None):
                res.append((curr2.val+carry)%10)
                carry = (curr2.val+carry)/10
                curr2=curr2.next
        if(carry):
            res.append(carry)
        return res
