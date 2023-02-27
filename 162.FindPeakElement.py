class Solution:
    def findPeakElement(self, nums):
        lower, upper = 0, len(nums)-1

        while lower < upper:
            mid = (lower+upper)//2
            if nums[mid] > nums[mid+1]:
                upper = mid
            else:
                lower = mid+1
        return lower 
