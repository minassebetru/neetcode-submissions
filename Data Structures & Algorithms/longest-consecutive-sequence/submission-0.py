class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 1
        currmax = 1

        if nums:
            for i in range(len(nums) - 1):
                if nums[i + 1] == (nums[i] + 1):
                    count += 1
                elif nums[i + 1] == nums[i]:
                    count = count
                else:
                    currmax = max(currmax, count)
                    count = 1
            

            return max(currmax, count)
        return 0