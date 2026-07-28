class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Frequency of characters in t
        target = {}

        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        window = {}

        left = 0
        minLen = float("inf")
        ans = ""

        # Number of characters matched
        matched = 0

        for right in range(len(s)):

            # Add current character
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # If this character is needed and hasn't exceeded the required count
            if ch in target and window[ch] <= target[ch]:
                matched += 1

            # If all characters of t are matched
            while matched == len(t):

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    ans = s[left:right+1]

                # Remove left character
                leftChar = s[left]

                if leftChar in target and window[leftChar] <= target[leftChar]:
                    matched -= 1

                window[leftChar] -= 1
                left += 1

        return ans