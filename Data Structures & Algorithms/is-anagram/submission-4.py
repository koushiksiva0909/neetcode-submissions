class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=sorted(s)
        t=sorted(t)
        isanagram=True
        for i,j in zip(s,t):
            if i!=j:
                isanagram=False
                break
        return isanagram
        