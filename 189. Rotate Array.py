class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotateArr(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

        k = k % len(nums)
        rotateArr(0, len(nums)-1)
        rotateArr(0, k-1)
        rotateArr(k, len(nums)-1)


        
