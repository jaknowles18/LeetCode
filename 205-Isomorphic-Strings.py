class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_maps = defaultdict(str)
        t_maps = defaultdict(str)

        if len(s) != len(t):
            return False
        
        for i in range(0, len(s)):
            if s_maps[s[i]] == "" and t_maps[t[i]] == "":
                s_maps[s[i]] = t[i]
                t_maps[t[i]] = s[i]
                continue
            
            if s_maps[s[i]] != t[i] or t_maps[t[i]] != s[i]:
                return False
            
        return True