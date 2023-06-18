class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        # taking the difference of sum of range and sum of nums array, the result should be the missing value
        return sum(range(len(nums)+1)) - sum(nums)
