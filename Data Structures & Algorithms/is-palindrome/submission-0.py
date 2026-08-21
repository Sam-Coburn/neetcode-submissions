class Solution:
    def isPalindrome(self, s: str) -> bool:
        scrubbed_str = ''

        char_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        for c in s.lower():
            if c in char_set:
                scrubbed_str = scrubbed_str + c

        return scrubbed_str == scrubbed_str[::-1]