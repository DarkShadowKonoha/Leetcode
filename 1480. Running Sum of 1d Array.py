class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = list()
        runningSum.append(nums[0])
        # print(runningSum[0])
        for i in range(1, len(nums)):
            runningSum.append(nums[i] + runningSum[i-1])

        return runningSum
