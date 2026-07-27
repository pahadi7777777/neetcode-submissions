class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        windowCount = [0] * 26

        # Frequency of s1
        for ch in s1:
            s1Count[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):
            windowCount[ord(s2[right]) - ord('a')] += 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                windowCount[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # Compare both frequency arrays
            if windowCount == s1Count:
                return True

        return False