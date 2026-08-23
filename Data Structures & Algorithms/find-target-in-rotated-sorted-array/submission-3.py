class Solution:
    def search(self, nums: List[int], target: int) -> int:

        hashmap = {}

        for i in range(len(nums)):
            hashmap[i] = nums[i]

        print(hashmap)

        for index, value in hashmap.items():
            if value == target:
                return index

        return -1