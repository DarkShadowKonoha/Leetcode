class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)

        ans = {}

        ans[0] = count['z']
        ans[2] = count['w']
        ans[4] = count['u']
        ans[6] = count['x']
        ans[8] = count['g']
        ans[3] = count['h'] - ans[8]
        ans[5] = count['f'] - ans[4]
        ans[7] = count['v'] - ans[5]
        ans[9] = count['i'] - ans[5] - ans[6] - ans[8]
        ans[1] = count['o'] - ans[0] - ans[2] - ans[4]

        output = ""

        for i in range(10):
            output += str(i) * ans[i]

        return output
