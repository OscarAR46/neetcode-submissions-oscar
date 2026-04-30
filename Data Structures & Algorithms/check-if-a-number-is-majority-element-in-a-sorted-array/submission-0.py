class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # 0 - not binary
        number_counter = {}

        for num in nums:
            if num not in number_counter:
                number_counter[num] = 1
            else:
                number_counter[num] += 1

        if target in number_counter:
            return number_counter[target] > len(nums) // 2
        
        return False

                