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
        if(l1==None):
            return l2
        elif(l2==None):
            return l1
        else:
            head=l1
            carry_bit = (l1.val+l2.val)//10
            l1.val = (l1.val+l2.val)%10
            while(l1.next != None and l2.next != None):
                carry_bit += l1.next.val+l2.next.val
                l1.next.val = carry_bit%10
                carry_bit = carry_bit//10
                l1 = l1.next
                l2 = l2.next
            if(l1.next == None):
                l1.next = l2.next
            while(l1.next != None):
                carry_bit += l1.next.val
                l1.next.val = carry_bit%10
                carry_bit = carry_bit//10
                l1 = l1.next
            if(carry_bit > 0):
                l1.next = ListNode(carry_bit)
            return head
