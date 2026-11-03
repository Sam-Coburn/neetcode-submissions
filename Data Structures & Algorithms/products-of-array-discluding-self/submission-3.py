class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # w/ Division
        count_zeroes = 0
        product = 1

        for n in nums:
            if n != 0:
                product *= n
            else:
                count_zeroes += 1

        if count_zeroes > 1:
            return [0] * len(nums)    

        result = list()

        for n in nums:
            if count_zeroes > 0:
                if n == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // n)
            

        return result