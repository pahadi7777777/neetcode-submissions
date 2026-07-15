class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def word_count(n):
            char_count ={}
            for char in n:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count
        
        return word_count(s) == word_count(t)
                

        # s_count = {}
        # for char in s:
        #     if char in s_count:
        #         s_count[char] += 1
        #     else:
        #         s_count[char] = 1

        # t_count = {}
        # for char in t:
        #     if char in t_count:
        #         t_count[char] += 1
        #     else:
        #         t_count[char] = 1
        
        # return s_count == t_count
        