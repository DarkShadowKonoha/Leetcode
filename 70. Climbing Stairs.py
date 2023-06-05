# class Solution:
#     def climbStairs(self, n):
#         f1, f2 = 1, 2
#         for i in range(n-1):
#             f1, f2 = f2, f1+f2
#         return f1

    class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp

        return one
