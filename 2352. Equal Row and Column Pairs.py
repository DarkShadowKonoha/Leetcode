class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = collections.Counter()

        for row in grid:
            counter[tuple(row)] += 1

        total = 0
        n = len(grid)
        for i in range(n):
            cur = []
            for j in range(n):
                cur.append(grid[j][i])
            total += counter[tuple(cur)]
        return total
