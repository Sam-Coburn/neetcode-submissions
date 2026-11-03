from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_freq = Counter(nums)

        result = list()
        while len(result) < k:
            max_freq = max(list(n_freq.values()))
            max_n = [k for k,v in n_freq.items() if v == max_freq][0]
            result.append(max_n)

            del n_freq[max_n]

        return result