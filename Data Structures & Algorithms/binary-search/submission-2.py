from math import floor, ceil

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left >= right:
                if left <= len(nums) - 1 and nums[left] == target:
                    return left
                if right >= 0 and nums[right] == target:
                    return right
                else:
                    return -1
            else:
                if (left + right) % 2 == 0:
                    mid = (left + right) // 2

                    if target == nums[mid]:
                        return mid
                    elif target < nums[mid]:
                        return binary_search(nums, target, left, mid - 1)
                    else:
                        return binary_search(nums, target, mid + 1, right)
                else:
                    mid = (left + right) / 2
                    mid_l = floor(mid)
                    mid_r = ceil(mid)

                    if target == nums[mid_l]:
                        return mid_l
                    elif target == nums[mid_r]:
                        return mid_r
                    elif target < nums[mid_l]:
                        return binary_search(nums, target, left, mid_l - 1)
                    elif target > nums[mid_r]:
                        return binary_search(nums, target, mid_r + 1, right)
                    else:
                        return -1

        return binary_search(nums, target, 0, len(nums) - 1)