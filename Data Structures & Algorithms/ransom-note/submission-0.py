class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag = {}

        for char in magazine:
            mag[char] = mag.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in mag or mag[char] == 0:
                return False
            mag[char] -= 1
        
        return True