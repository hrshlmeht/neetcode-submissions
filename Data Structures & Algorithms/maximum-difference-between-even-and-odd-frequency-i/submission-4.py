from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)

        odd_counts = []
        even_counts = []

        for count in counts.values():
            if count % 2 == 1:
                odd_counts.append(count)
            else:
                even_counts.append(count)

        return max(odd_counts) - min(even_counts)