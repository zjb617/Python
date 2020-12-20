import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t) - collections.Counter(s)).elements())[0]