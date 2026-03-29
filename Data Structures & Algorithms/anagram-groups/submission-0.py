class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            sorted_word_key = tuple(sorted(i))
            if sorted_word_key not in anagrams:
                anagrams[sorted_word_key] = []
            anagrams[sorted_word_key].append(i)

        return list(anagrams.values())