class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Times solved from memory = 0
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle = L + (R - L) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                R = middle - 1
            else:
                L = middle + 1
        return L

