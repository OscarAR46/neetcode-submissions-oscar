class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Times solved from memory = 0
        smallest_num = nums[0]
        L = 0
        R = len(nums) - 1

        while L <= R:
            if nums[L] < nums[R]:
                smallest_num = min(smallest_num, nums[L])
                break

            middle = L + (R - L) // 2
            smallest_num = min(smallest_num, nums[middle])
            if nums[middle] >= nums[L]:
                L = middle + 1
            else:
                R = middle - 1
        return smallest_num