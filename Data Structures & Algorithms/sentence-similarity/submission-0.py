class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # Step 1: early exit
        if len(sentence1) != len(sentence2):
            return False
        
        # Step 2: build pair set with both directions
        pair_set = set()
        for pair in similarPairs:
            pair_set.add((pair[0], pair[1]))
            pair_set.add((pair[1], pair[0]))
        
        # Step 3: check each word pair
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and (w1, w2) not in pair_set:
                return False
        
        return True