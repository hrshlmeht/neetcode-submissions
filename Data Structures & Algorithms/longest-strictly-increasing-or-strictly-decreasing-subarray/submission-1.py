class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ansList = []

        counter = 1
        #inc 
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                counter += 1
            else:
                ansList.append(counter)
                counter = 1
        ansList.append(counter)
        counter = 1
        
        #dec
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                counter += 1
            else:
                ansList.append(counter)
                counter = 1
        
        ansList.append(counter)
        
        return max(ansList)
