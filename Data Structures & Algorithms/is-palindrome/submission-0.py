class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L, R = 0, len(s) - 1
        while L < R:
            if s[L].isalnum() == False:
                L += 1
                continue
            if s[R].isalnum() == False:
                R -= 1
                continue
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        return True