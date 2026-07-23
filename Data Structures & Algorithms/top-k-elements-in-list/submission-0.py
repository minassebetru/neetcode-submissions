class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        pairs = {}
        for num in nums:
            pairs[num] = pairs.get(num, 0) + 1

        freq = []
        for i in range(k):
            max_key = max(pairs, key=pairs.get)
            freq.append(max_key)
            del pairs[max_key]

        return freq