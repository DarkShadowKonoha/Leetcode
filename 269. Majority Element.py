from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        # print(numCount))
        size = len(nums)
        for key in numCount:
            if numCount[key] > size/2:
                return key
        
