# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: no lists
        if not lists:
            return None

        k = len(lists)

        # Distance between 2 lists/groups we want to merge
        interval = 1

        # Keep merging until interval becomes >= number of lists
        while interval < k:
            # Merge pairs:
                # interval = 1 -> (0,1), (2,3), (4,5)...
                # interval = 2 -> (0,2), (4,6)...
                # interval = 4 -> (0,4)...
            for i in range(0, k - interval, interval * 2):

                lists[i] = self.mergeTwo(
                    lists[i],
                    lists[i + interval]
                )

            # After each round, each merged group becomes twice as large
            interval *= 2

        # Fully merged list will be stored at index 0
        return lists[0]

    # Helper function to merge 2 sorted lists
    def mergeTwo(self, l1, l2) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next #always update current
        #attach remaining nodes to current
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next
