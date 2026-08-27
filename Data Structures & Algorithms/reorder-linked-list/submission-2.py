# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            # find the mid element (second one if even)
    # we will have two linked list now, break opne after mid
    # keep l1 same, and reverse the 2nd linked list
    # one at a time link the both lists

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now head of list2
        second = slow.next
        # end the list 1
        slow.next = None

        # now reverse list 2
        prev, curr1 = None, second
        while curr1:
            temp = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = temp
        second = prev

        # now merge both the list
        list1 = head
        list2 = second


        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2


        