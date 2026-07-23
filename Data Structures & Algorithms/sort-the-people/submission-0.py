class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        data = dict(zip(heights, names))

        names = sorted(data, reverse = True)

        return [data[h] for h in names]