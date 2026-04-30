class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 0
        def is_palindrome(L, R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
            return True

        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return (is_palindrome(L + 1, R) or
                        is_palindrome(L, R - 1))
            L += 1
            R -= 1

        return True