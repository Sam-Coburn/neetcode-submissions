class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create Dict with Index of Each Value
        i_dict = {}

        for i in range(len(nums)):
            curr = nums[i]

            if curr not in i_dict.keys():
                i_dict[curr] = [i]
            else:
                i_dict[curr].append(i)

        # Iterate Through List and Find Indices of Needed Val
        for i in range(len(nums)):
            curr = nums[i]
            needed_val = target - curr

            if needed_val in i_dict.keys():
                if curr == needed_val and len(i_dict[needed_val]) > 1:
                    return sorted([i, i_dict[needed_val][-1]])
                if curr == needed_val and len(i_dict[needed_val]) == 1:
                    continue
                else:
                    return sorted([i, i_dict[needed_val][0]])