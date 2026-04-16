class Solution:
    def isPalindrome(self, s: str) -> bool:
    # 2
        s = s.lower()
        L, R = 0, len(s) - 1
        # as per question, if not isalnum (== False) skip to next alphanumeric char to 
        # continue palindrome check
        while L < R:
            if s[L].isalnum() == False:
                L += 1
                continue
            if s[R].isalnum() == False:
                R -= 1
                continue
            # now palindrome check for question is done
            if s[L] == s[R]:
                L += 1
                R -= 1
                continue
            else:
                return False
        return True


