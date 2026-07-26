class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxFreq = 0
        result = 0

        for right in range(len(s)):
            # Add current character to the frequency map
            count[s[right]] = 1 + count.get(s[right], 0)

            # Update the highest frequency in the current window
            maxFreq = max(maxFreq, count[s[right]])

            # If the window is invalid, shrink it
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            # Update the maximum valid window size
            result = max(result, right - left + 1)

        return result
