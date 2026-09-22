class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
    
        for word in strs:
        # Sort the word to use as key
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
        return list(anagram_map.values())


        