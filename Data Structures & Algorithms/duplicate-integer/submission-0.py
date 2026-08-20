class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()

        for n in nums:
            if n not in seen_set:
                seen_set.add(n)
            else:
                return True

        return False