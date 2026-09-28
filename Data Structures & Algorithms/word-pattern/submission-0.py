class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern) != len(word):
            return False

        cha_to_wrd = {}
        wrd_to_cha = {}

        for c,w in zip(pattern,word):
            if c in cha_to_wrd:
                if cha_to_wrd[c] != w:
                    return False
            else:
                if w in wrd_to_cha:
                    return False
                cha_to_wrd[c] = w
                wrd_to_cha[w] = c
        return True