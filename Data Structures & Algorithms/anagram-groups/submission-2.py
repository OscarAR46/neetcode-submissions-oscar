class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for word in strs:
            word_sorted = tuple(sorted(word))
            if word_sorted not in anagrams_dict:
                anagrams_dict[word_sorted] = [word]
            else:
                anagrams_dict[word_sorted].append(word)

        return list(anagrams_dict.values())