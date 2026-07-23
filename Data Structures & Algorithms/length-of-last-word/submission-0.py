class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        strings = s.split()
        last = len(strings[-1])
        return last