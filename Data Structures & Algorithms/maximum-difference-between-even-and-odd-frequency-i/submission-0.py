class Solution:
    def maxDifference(self, s: str) -> int:
        
        dic = Counter(list(s))
        evens = []
        odds = []

        for val in dic.values():
            if val % 2 == 0:
                evens.append(val)
            elif val % 2 == 1:
                odds.append(val)
        
        diff = max(odds) - min(evens)
        
        return diff