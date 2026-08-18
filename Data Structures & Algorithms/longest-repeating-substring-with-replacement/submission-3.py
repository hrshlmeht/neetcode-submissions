class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charCount = {}
        left = 0
        maxFreq = 0
        answer = 0

        for right in range(len(s)):

            # Add current character
            charCount[s[right]] = charCount.get(s[right], 0) + 1

            # Highest frequency character in current window
            maxFreq = max(maxFreq, charCount[s[right]])

            # Number of replacements needed
            windowLength = right - left + 1

            if windowLength - maxFreq > k:
                charCount[s[left]] -= 1
                left += 1

            # Current valid window
            answer = max(answer, right - left + 1)

        return answer