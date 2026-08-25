class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        final_list = []


        for i in nums1:
            final_list.append(i)


        for j in nums2:
            final_list.append(j)


        final_list.sort()

        n = len(final_list)

        # If odd number of elements
        if n % 2 == 1:
            return final_list[n // 2]

        # If even number of elements
        else:
            middle1 = final_list[n // 2 - 1]
            middle2 = final_list[n // 2]

            return (middle1 + middle2) / 2

        