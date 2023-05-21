from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        countDict = Counter(nums)
        for i in countDict.values():
            if i > 1:
                return True
        return False
