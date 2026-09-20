class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1 

        yolo = {}

        for i in range(len(nums)):
            if nums[i] not in yolo:
                yolo[nums[i]] = []

            yolo[nums[i]].append(i)

        for i in yolo:
            #print(i)
             if i == target:
                return min(yolo[i])

