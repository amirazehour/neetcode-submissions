class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1= dict(enumerate(s))
        d2= dict(enumerate(t))
        # {0:a;1:b} d1
        
        return sorted(d1.values())==sorted(d2.values())
        