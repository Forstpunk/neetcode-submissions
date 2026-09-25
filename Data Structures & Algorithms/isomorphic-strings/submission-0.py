class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        
        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:      # s char maps to different t char
                    return False
            else:
                if ct in t_to_s:          # t char already mapped from different s char
                    return False
                s_to_t[cs] = ct
                t_to_s[ct] = cs
        
        return True