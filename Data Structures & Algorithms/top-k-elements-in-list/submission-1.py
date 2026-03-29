class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a_dict = {}
        for i in nums:
            if i not in a_dict:
                a_dict[i] = 1
            a_dict[i] += 1
        
        return sorted(a_dict, key=a_dict.get, reverse=True)[:k]