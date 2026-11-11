class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        d1= dict(enumerate(s))
        d2= dict(enumerate(t))
        # {0:a;1:b} d1
        
        return d1 == d2
        