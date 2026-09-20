class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##brute force hashmap solution
        # if target not in nums:
        #     return -1 

        # yolo = {}

        # for i in range(len(nums)):
        #     if nums[i] not in yolo:
        #         yolo[nums[i]] = []

        #     yolo[nums[i]].append(i)

        # for i in yolo:
        #     #print(i)
        #      if i == target:
        #         return min(yolo[i])

        ##start with the binary search solution

        l = 0 
        r  = len(nums)-1

        while l <= r:
            m = (l+r) //2 
            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m+1 
            else:
                return m
        
        return -1


