class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solved from memory = 1
        counter = {}
        for number in nums:
            if number not in counter:
                counter[number] = 1
            counter[number] += 1
        return max(counter, key=counter.get)

# Can solve in linear time and O(1) space next? above not very efficient (O(n) & O(n))