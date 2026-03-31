class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute force time = O(n2) if square or most likely O(m x n) & space = O(1)
        # Will use binary search to solve for time = O(log(m x n))
        for row in matrix:
            for item in row:
                if item == target:
                    return True
        return False
                