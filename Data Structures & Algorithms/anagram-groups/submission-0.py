class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword in groups:
                groups[sortedword].append(word)
            else:
                groups[sortedword] = [word]
        return list(groups.values())