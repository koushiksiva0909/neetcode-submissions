class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen={}
        mag_seen={}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in seen:
                seen[ransomNote[i]]=1
            else : 
                seen[ransomNote[i]]+=1
        for i in range(len(magazine)):
            if magazine[i] not in mag_seen:
                mag_seen[magazine[i]]=1
            else :
                mag_seen[magazine[i]]+=1
        for i in seen:
            if i not in mag_seen:
                return False
            if seen[i] > mag_seen[i]:
                return False
        return True
        