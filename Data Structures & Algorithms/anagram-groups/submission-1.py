class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for i in strs:
            sorted_string = tuple(sorted(i))
            if sorted_string not in anagrams_dict:
                anagrams_dict[sorted_string] = [i]
            else:
                anagrams_dict[sorted_string].append(i)

        return list(anagrams_dict.values())