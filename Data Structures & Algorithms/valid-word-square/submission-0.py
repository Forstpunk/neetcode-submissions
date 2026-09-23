class Solution:
    def validWordSquare(self, words: list) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                # bounds check before accessing words[j][i]
                if j >= len(words) or i >= len(words[j]):
                    return False
                # symmetry check
                if words[i][j] != words[j][i]:
                    return False
        return True