class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        posn = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[posn] = nums[i]
                posn+=1
        while posn < len(nums):
            nums[posn]=0
            posn+=1
        
