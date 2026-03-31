class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Completed from memory = 2
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle = L + (R - L) // 2
            if target < nums[middle]:
                R = middle - 1
            elif target > nums[middle]:
                L = middle + 1
            else:
                return middle
        return -1