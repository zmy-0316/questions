"""
1-9中满足个数是k，和为n的所有组合；
1.一个数组组合问题，不可重复使用，需要startindex；
2.记录当前和需要另加一个变量，cur_sum

3.剪枝：cur_sum > targetsum；k个数的组合，遍历到n - (k - len(path))
"""
class Solution:
    def combine(self, n, k):
        result = []
        self.backtracking(n, 1, 0, k, [], result)
        return result
    def backtracking(self, targetsum, startindex, cur_sum, k, path, result):
        if cur_sum > targetsum:
            return
        if len(path) == k and cur_sum == targetsum:
            result.append(path[:])
            return
        for i in range(startindex, 9 - (k - len(path)) + 1):
            path.append(i)
            cur_sum += i
            self.backtracking(targetsum, i + 1, cur_sum, k, path, result)
            cur_sum -= i
            path.pop()


solution = Solution()
print(solution.combine(9, 3))
