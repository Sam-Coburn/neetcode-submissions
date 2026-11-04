class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        char_set = set()
        max_len = 0

        l = 0
        for r in range(0, len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            max_len = max(r - l + 1, max_len)

        return max_len