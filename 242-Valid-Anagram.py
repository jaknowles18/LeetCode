class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        len1 = len(s)
        len2 = len(t)

        if len1 != len2:
            return False

        for letters1, letters2 in zip(s, t):
            dic1[letters1] = dic1.get(letters1, 0) + 1
            dic2[letters2] = dic2.get(letters2, 0) + 1
        
        return dic1 == dic2



