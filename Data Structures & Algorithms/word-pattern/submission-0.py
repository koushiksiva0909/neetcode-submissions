class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        seen_patt={}
        seen_word={}
        if len(word)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in seen_patt:
                if word[i] in seen_word:
                    return False
                seen_patt[pattern[i]]=word[i]
                seen_word[word[i]]=pattern[i]
            else :
                if seen_patt[pattern[i]] != word[i]:
                    return False
        return True  