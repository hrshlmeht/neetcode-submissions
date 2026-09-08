class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        nums_sorted = sorted(nums, reverse = True)
        nums_sorted_asc = sorted(nums)

        if nums == nums_sorted_asc or nums == nums_sorted:
            return True
        
        else:
            return False