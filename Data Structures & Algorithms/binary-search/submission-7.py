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

        left = 0 
        right  = len(nums)-1

        while left <= right:
            mid = (left +right) //2 
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1 
            else:
                return mid
        
        return -1


