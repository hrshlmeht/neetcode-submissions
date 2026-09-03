class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        boom_boom = {}
        ans = []

        # Count frequencies
        for i in range(len(nums)):
            if nums[i] in boom_boom:
                boom_boom[nums[i]] += 1
            else:
                boom_boom[nums[i]] = 1

        # Sort numbers based on frequency
        sorted_boom = sorted(
            boom_boom,
            key=boom_boom.get,
            reverse=True
        )

        # Take top k
        for i in range(k):
            ans.append(sorted_boom[i])

        return ans