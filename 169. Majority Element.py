# from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            count += (1 if n == res else -1)
        
        return res
        
        
        # Using the extra space

        # numCount = Counter(nums)
        # # print(numCount))
        # size = len(nums)
        # for key in numCount:
        #     if numCount[key] > size/2:
        
