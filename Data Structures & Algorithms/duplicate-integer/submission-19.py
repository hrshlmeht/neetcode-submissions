class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_pro = set(nums)

        if len(nums_pro) == len(nums):
            return False
        else:
            return True
        