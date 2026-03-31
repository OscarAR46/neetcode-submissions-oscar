# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
# SUBMIT AND SOLVE AGAIN TO CEMENT
class Solution:
    def guessNumber(self, n: int) -> int:
        # Completed from memory = 2
        L = 0
        R = n
        while True:
            middle = L + (R - L) // 2
            result = guess(middle)
            # If result (middle number) is 1 (as > than 0) means its lower than picked num so we move L
            if result > 0:
                L = middle + 1
            elif result < 0:
                R = middle -1
            else:
                return middle
                