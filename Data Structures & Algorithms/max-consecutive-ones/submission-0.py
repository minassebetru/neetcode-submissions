class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if 0 not in nums:
            return len(nums)
        
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count