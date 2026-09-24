class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strings:
            t = tuple((ord(s[i+1]) - ord(s[i])) % 26 for i in range(len(s)-1))
            groups[t].append(s)
        return list(groups.values())


        