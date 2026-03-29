# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
# SUBMIT AND SOLVE AGAIN TO CEMENT
class Solution:
    def guessNumber(self, n: int) -> int:
        L = 1
        R = n
        while True:
            mid = L + (R - L) // 2
            res = guess(mid)

            if res > 0:
                L = mid + 1
            elif res < 0:
                R = mid - 1
            else:
                return mid


"""
within this, 1 - n is range so L = 1 and R = n
guess() is the defined func returning:
    0 if == pick
    1 if num = lower than pick
    -1 if num = higher than pick
use return True as we are GUARENTEED to find num, use while L > x if not
"""