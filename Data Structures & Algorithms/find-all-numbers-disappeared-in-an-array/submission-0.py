class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        missing = []
        x = 1 
        
        while x <= len(nums):
            if x not in nums:
                missing.append(x)
            x += 1
        
        return missing