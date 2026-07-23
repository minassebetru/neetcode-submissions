class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        pairs = {}
        for num in nums:
            if num in pairs:
                pairs[num] += 1
            else:
                pairs[num] = 1

        nums.sort(key=lambda x: (pairs[x], -x))

        return nums
        

        