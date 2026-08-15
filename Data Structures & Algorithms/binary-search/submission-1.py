class Solution:
    def search(self, nums: List[int], target: int) -> int:

        location = {}

        for i in range(0 , len(nums)):
            location[i] = nums[i]
        

        for i in range(0 , len(nums)):
            if target == location[i]:
                return i
        

        return -1

    


        