class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, n):
            currways = 0
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                currways += dp[-2]
            if s[i] != '0':
                currways += dp[-1]
            if currways == 0:
                return 0
            dp.append(currways)
        
        return dp[-1]
