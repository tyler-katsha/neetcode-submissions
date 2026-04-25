class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        ht1 = {}
        ht2 = {}
        n,m,i = len(s),len(t),0
        
        while i < n or i < m:
            if s[i] not in ht1:
                ht1[s[i]] = 0 
            else:
                ht1[s[i]] += 1
            if t[i] not in ht2:
                ht2[t[i]] = 0
            else:
                ht2[t[i]] += 1
            
            i+=1

        if ht1 == ht2:
            return True
        
        return False

        