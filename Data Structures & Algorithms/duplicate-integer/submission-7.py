class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num = set(nums)
        print(num)
        print (len(num))
        print (len(nums))
        if len(num) == len(nums):
            return False
        else:
            return True
             
        