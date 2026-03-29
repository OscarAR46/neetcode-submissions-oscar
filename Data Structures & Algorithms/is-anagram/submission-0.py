class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(sorted(s))
        t_list = list(sorted(t))
        if s_list == t_list:
            return True
        return False