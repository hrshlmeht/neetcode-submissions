# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        groups = self.countKGroups(head,k)

        if groups == 0:
            return head
        
        current_group = 0

        current = head

        previous_reversed_group_last_node = None

        while current:
            
            reversed_group_head, first_node_before_reversal, node_of_next_k_group = self.reverseGroup(current, k)

            if previous_reversed_group_last_node is not None:
                previous_reversed_group_last_node.next = reversed_group_head
            
            current_group += 1

            if current_group == 1:
                head = reversed_group_head

            if current_group == groups:
                first_node_before_reversal.next = node_of_next_k_group
                break
            
            current = node_of_next_k_group
            previous_reversed_group_last_node = first_node_before_reversal
        
        return head

    def countKGroups(self, head:Optional[ListNode], k:int) -> int:
        groups = 0
        current = head
        counter = 0

        while current:
            counter += 1
            
            if counter == k:
                groups += 1
                counter = 0

            current = current.next

        return groups 

    def reverseGroup(self, head:Optional[ListNode], k:int)->Tuple[ListNode, ListNode, ListNode]:

        if head is None:
            return (None, None, None)
        
        counter = 0
        current = head
        prev = None

        first_node_before_reversal = current
        node_of_next_k_group = None

        if k == 1:
            return (head, head, head.next)

        while current:
            counter += 1
            
            next_node = current.next

            current.next = prev
            prev = current
            current = next_node

            if counter == k:
                node_of_next_k_group = next_node
                break
        
        return (prev, first_node_before_reversal, node_of_next_k_group)