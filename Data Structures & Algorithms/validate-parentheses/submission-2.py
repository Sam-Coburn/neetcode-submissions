class Solution:
    def isValid(self, s: str) -> bool:
        left_stack = list()

        for p in s:
            # Left Opener
            if p in {'{', '[', '('}:
                left_stack.append(p)
            # Right Closer
            else:
                if len(left_stack) > 0:
                    left_val = left_stack.pop()
                else:
                    return False

                if left_val == '{' and p == '}':
                    continue
                elif left_val == '[' and p == ']':
                    continue
                elif left_val == '(' and p == ')':
                    continue
                else:
                    return False

        return len(left_stack) == 0

