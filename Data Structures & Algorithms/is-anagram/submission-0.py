from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        

        s_counter = Counter(s)
        t_counter = Counter(t)

        for k in s_counter.keys():
            s_count = s_counter[k]
            t_count = t_counter[k]

            if s_count != t_count:
                return False

        return True