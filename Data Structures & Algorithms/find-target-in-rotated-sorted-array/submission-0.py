class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 0
        L = 0
        R = len(nums) - 1

        while L < R:
            mid = L + (R - L) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        pivot = L

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid2 = left + (right - left) // 2
                if nums[mid2] == target:
                    return mid2
                elif nums[mid2] < target:
                    left = mid2 + 1
                else:
                    right = mid2 - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)