class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = 0
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i],"",1)
                count += 1
        if count == len(s):
            return True
        else:
            return False
