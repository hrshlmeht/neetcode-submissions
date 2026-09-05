class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # 1. Create a new sorted copy (ascending order)
        expected = sorted(heights)
        
        # 2. Count the mismatches between the two lists
        mismatches = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatches += 1
                
        return mismatches