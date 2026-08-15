class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set_nums = set(nums)

        # if len(set_nums) == len(nums):
        #     return False
        # else:
        #     return True
        
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False

            
            
            

        