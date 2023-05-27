class Solution:
    def fib(self, n: int) -> int:
        f1, f2 = 0, 1
        if n == 0:
            return f1
        if n == 1:
            return f2

        return self.fib(n-1) + self.fib(n-2)
