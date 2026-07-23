class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_list, t_list = list(s), list(t)
        for letter in s_list:
            if letter in s_list and letter in t_list:
                t_list.remove(letter)
        if len(t_list) == 0:
            return True
        return False