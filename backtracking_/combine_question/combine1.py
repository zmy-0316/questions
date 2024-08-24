"""
回溯--组合问题1
题目：给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。示例: 输入: n = 4, k = 2 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
关键点：
1.不可重复用元素，要有startindex；
2.剪枝，由于k个组合，当启示遍历点之后的元素数量不满足k个时就没必要遍历了，具体截止到n - (k - len(path))
"""
class Solution:
    def combine(self, n, k):
        result = []
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startindex,  path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startindex, n - (k - len(path)) + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()

solution = Solution()
print(solution.combine(5, 2))
