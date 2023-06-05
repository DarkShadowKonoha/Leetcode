class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Using HashMap instead of a simple tree
        res = []
        perm = []
        count = { n:0 for n in nums }
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs()

                    count[n] += 1
                    perm.pop()

        dfs()
        return res
