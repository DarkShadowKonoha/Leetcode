class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        len_nums = len(nums)
        sums = [0]*len_nums
        sums[0] = nums[0]
        max_sum = sums[0]

        for i in range(1, len_nums):
            sums[i] = sums[i-1] + nums[i] if nums[i] > nums[i-1] else nums[i]
            max_sum = max(sums[i], max_sum)

        return max_sum
